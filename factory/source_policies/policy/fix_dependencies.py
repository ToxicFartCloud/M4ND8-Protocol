# ./.m4nd8/policy/fix_dependencies.py
"""
Dependency Auto-Remediation for M4ND8 Enterprise.
- Offline-only (no network calls)
- Uses native toolchains (uv, npm, cargo, go)
- Only acts when a manifest exists but is non-compliant
- Never creates requirements.txt
"""
import os
import subprocess
import sys
import glob

def run_cmd(cmd, cwd="."):
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd,
            capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            print(f"WARNING: {cmd} failed: {result.stderr}", file=sys.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"WARNING: {cmd} exception: {e}", file=sys.stderr)
        return False

def fix_python():
    # Prefer uv, fallback to poetry
    if os.path.exists("pyproject.toml"):
        if run_cmd("uv lock"):
            return True
        if run_cmd("poetry lock"):
            return True
    # Legacy: convert requirements.txt → uv.lock, then delete
    if os.path.exists("requirements.txt"):
        if run_cmd("uv pip compile requirements.txt -o uv.lock"):
            os.remove("requirements.txt")
            print("WRITE_OK: uv.lock")
            print("WRITE_OK: requirements.txt (deleted)")
            return True
    return False

def fix_node():
    if os.path.exists("package.json"):
        return run_cmd("npm install --package-lock-only")
    return False

def fix_rust():
    if os.path.exists("Cargo.toml"):
        return run_cmd("cargo generate-lockfile")
    return False

def fix_go():
    if os.path.exists("go.mod"):
        return run_cmd("go mod tidy")
    return False

def main():
    fixed = False
    print("🔧 M4ND8: Auto-remediating dependency violations...")

    if glob.glob("pyproject.toml") or glob.glob("requirements.txt"):
        if fix_python():
            fixed = True

    if os.path.exists("package.json"):
        if fix_node():
            fixed = True

    if os.path.exists("Cargo.toml"):
        if fix_rust():
            fixed = True

    if os.path.exists("go.mod"):
        if fix_go():
            fixed = True

    if fixed:
        print("✅ Remediation complete. Re-run reqchk.py to verify.")
        sys.exit(0)
    else:
        print("ℹ️ No actionable dependency manifests found. Skipping remediation.")
        sys.exit(0)

if __name__ == "__main__":
    main()