# .m4nd8/policy/reqchk.py
"""
Phase 1: Requirements Conformance Audit
- Checks requirements.txt (Python) and package.json (Node/NPM)
- Verifies exact versions against .m4nd8/data/approved_dependencies.db
- Stops process if unapproved dependencies are found
"""
import os
import sys
import json
import sqlite3
import re

# --- 1. Database Connection ---
def check_against_db(ecosystem, package, version):
    """Returns True if the specific package version is in the allowed DB."""
    db_path = ".m4nd8/data/approved_dependencies.db"
    
    if not os.path.exists(db_path):
        return False, "Database not found. Run update_adb.py first."

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check for exact match
        cursor.execute("""
            SELECT 1 FROM approved_versions 
            WHERE ecosystem=? AND package=? AND version=?
        """, (ecosystem, package, version))
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return True, None
        else:
            return False, f"Not Approved: {ecosystem} -> {package} {version}"
            
    except sqlite3.Error as e:
        return False, f"DB Error: {e}"

# --- 2. Check Python (requirements.txt) ---
def check_python_requirements():
    violations = []
    if not os.path.exists("requirements.txt"):
        return violations

    print("   📄 Checking requirements.txt...")
    with open("requirements.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            # We strictly expect format: package==version
            if "==" in line:
                # remove comments like "flask==2.0.1 # core"
                clean_line = line.split("#")[0].strip()
                try:
                    pkg, ver = clean_line.split("==", 1)
                    pkg = pkg.strip()
                    ver = ver.strip()
                    
                    # CHECK THE DATABASE
                    is_ok, msg = check_against_db("pypi", pkg, ver)
                    if not is_ok:
                        violations.append(msg)
                except ValueError:
                    violations.append(f"Invalid format (must be pkg==ver): {line}")
            else:
                violations.append(f"Missing pinned version (no '=='): {line}")
    return violations

# --- 3. Check Node (package.json) ---
def check_node_package_json():
    violations = []
    if not os.path.exists("package.json"):
        return violations

    print("   📦 Checking package.json...")
    try:
        with open("package.json", "r") as f:
            data = json.load(f)
            
        # Check both dependencies and devDependencies
        all_deps = {}
        all_deps.update(data.get("dependencies", {}))
        all_deps.update(data.get("devDependencies", {}))

        for pkg, ver in all_deps.items():
            # Clean version string (remove ^ or ~ if present for strict checking)
            clean_ver = ver.replace("^", "").replace("~", "")
            
            # CHECK THE DATABASE
            is_ok, msg = check_against_db("npm", pkg, clean_ver)
            if not is_ok:
                violations.append(msg)
                
    except json.JSONDecodeError:
        violations.append("Failed to parse package.json (invalid JSON)")
    
    return violations

# --- 4. Main Execution ---
def main():
    print("🔍 M4ND8: Auditing dependencies against Approved DB...")
    
    all_violations = []
    
    # Run Checks
    all_violations.extend(check_python_requirements())
    all_violations.extend(check_node_package_json())

    # Report Results
    if all_violations:
        print("\n❌ HALT: Policy Violations Found:")
        for v in all_violations:
            print(f"   - {v}")
        print("\nACTION REQUIRED: Update these versions to match your approved_deps.json")
        sys.exit(1)
    else:
        print("\n✅ PASS: All dependencies are approved.")
        sys.exit(0)

if __name__ == "__main__":
    main()
