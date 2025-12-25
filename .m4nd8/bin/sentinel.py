# sentinel_executor.py (run by CI or human before merge)
import yaml
import os, subprocess, sys

# Royal Path Resolver: locate director.yaml in Factory or Capsule
base_dir = os.path.dirname(os.path.abspath(__file__))
possible_paths = [
    os.path.join(base_dir, "director.yaml"),       # Factory mode
    os.path.join(base_dir, "..", "director.yaml"), # Capsule mode
]
config_path = next((p for p in possible_paths if os.path.exists(p)), None)
if config_path is None:
    raise FileNotFoundError("director.yaml not found in expected locations. HALT.")

# Derive policy root from director.yaml location
policy_root = os.path.dirname(config_path)
compliance_path = os.path.join(policy_root, "policy", "compliance.yaml")

def main():
    with open("manifest.yaml") as f:
        manifest = yaml.safe_load(f)
    with open(compliance_path) as f:
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
