# File: .m4nd8/policy/reqchk.py
import json
import sys
import re
import urllib.request
import urllib.error

# CONFIGURATION
# We point to the public deps.dev API
API_BASE = "https://api.deps.dev/v3/systems/pypi/packages"
# This assumes the command is run from the project root
TARGET_REQ_FILE = "requirements.txt" 

def parse_requirements():
    """Parses requirements.txt for package names."""
    pkgs = []
    try:
        with open(TARGET_REQ_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                match = re.match(r"^([a-zA-Z0-9_\-]+)", line)
                if match:
                    pkgs.append(match.group(1))
    except FileNotFoundError:
        # If requirements.txt is missing, we might want to pass or fail 
        # depending on if the project is expected to have dependencies.
        # For strict governance, we warn but don't crash if it's just empty.
        print(f"NOTICE: {TARGET_REQ_FILE} not found. Skipping dependency check.")
        sys.exit(0) 
    return pkgs

def consult_oracle(package_name):
    """Queries deps.dev for the package metadata."""
    url = f"{API_BASE}/{package_name}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        print(f"WARNING: API Error for {package_name}: {e.code}")
        return None
    except Exception as e:
        print(f"WARNING: Connection error: {e}")
        return None

def audit_dependencies():
    packages = parse_requirements()
    if not packages:
        print("No packages to audit.")
        sys.exit(0)

    print(f"--- M4ND8 reqchk: Auditing {len(packages)} packages via deps.dev ---")
    
    violations = []
    
    for pkg in packages:
        print(f"[*] Checking: {pkg}...", end=" ")
        data = consult_oracle(pkg)
        
        if not data:
            print("FAIL")
            violations.append(f"[!] HALLUCINATION DETECTED: Package '{pkg}' does not exist in the public registry.")
            continue
            
        latest_version = ""
        for v in data.get('versions', []):
            if v.get('isDefault'):
                latest_version = v.get('versionKey', {}).get('version')
                break
        
        if latest_version:
            print(f"OK (Latest: {latest_version})")
        else:
            print("WARNING (No default version)")

    if violations:
        print("\nFATAL: Dependency Policy Violations Detected")
        for v in violations:
            print(v)
        sys.exit(1) # This triggers the HARD_STOP in M4ND8
    else:
        print("\nPASS: All dependencies verified.")
        sys.exit(0)

if __name__ == "__main__":
    audit_dependencies()
