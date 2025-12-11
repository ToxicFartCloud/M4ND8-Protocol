# sentinel_executor.py (run by CI or human before merge)
import yaml, subprocess, sys

def main():
    with open("compliance.yaml") as f:
        manifest = yaml.safe_load(f)

    with open(".m4nd8/policy/compliance.yaml") as f:
        checks = yaml.safe_load(f)["checks"]

    for chk in checks:
        # Evaluate applies_if using STRUCTURED data, not LLM
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
