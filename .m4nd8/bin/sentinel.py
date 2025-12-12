# sentinel_executor.py (run by CI or human before merge)
import yaml
import os, subprocess, sys

# Royal Path Resolver: locate director.yaml to derive project root
base_dir = os.path.dirname(os.path.abspath(__file__))
possible_director_paths = [
    os.path.join(base_dir, "..", "director.yaml"),   # Capsule mode (.m4nd8/bin/)
    os.path.join(base_dir, "director.yaml"),         # Factory mode (bin/)
]
director_path = next((p for p in possible_director_paths if os.path.exists(p)), None)
if director_path is None:
    raise FileNotFoundError("director.yaml not found in expected locations. HALT.")

# Derive project root from director.yaml location
project_root = os.path.dirname(director_path)
manifest_path = os.path.join(project_root, "manifest.yaml")
compliance_path = os.path.join(project_root, ".m4nd8", "policy", "compliance.yaml")

def main():
<<<<<<< HEAD
    with open("compliance.yaml") as f:
        manifest = yaml.safe_load(f)

    with open(".m4nd8/policy/compliance.yaml") as f:
=======
    with open(manifest_path) as f:
        manifest = yaml.safe_load(f)
    with open(compliance_path) as f:
>>>>>>> 145d3ca (Fixed some wiring issues)
        checks = yaml.safe_load(f)["checks"]
    for chk in checks:
        applies = True
        if "applies_if" in chk:
            cond = chk["applies_if"]
            feature = cond["feature"]
            applies = manifest.get("features", {}).get(feature, False)
        if applies:
            print(f"Running check: {chk['name']}")
            result = subprocess.run(
                chk["script"],
                shell=True,
                capture_output=True,
                text=True,
                timeout=chk.get("timeout_sec", 10)
            )
            if result.returncode != 0:
                print(f"HALT: {chk['name']} failed\n{result.stdout}\n{result.stderr}")
                sys.exit(1)
        else:
            print(f"Skipped: {chk['name']} (not applicable)")

if __name__ == "__main__":
    main()
