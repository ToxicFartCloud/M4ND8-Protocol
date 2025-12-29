#!/usr/bin/env python3
"""
adb_tool.py — Autonomous Dependency Base Manager
Usage: python3 adb_tool.py snapshot
"""
import sys
import os
import sqlite3
import json

# CONFIG
DB_PATH = ".m4nd8/data/approved_dependencies.db"

def init_db():
    # Ensure the directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # Create table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS approved_versions (
            ecosystem TEXT NOT NULL,
            package TEXT NOT NULL,
            version TEXT NOT NULL,
            PRIMARY KEY (ecosystem, package, version)
        )
    """)
    conn.commit()
    return conn

def snapshot_local():
    """Scans local manifests and updates the DB."""
    print("📸 Snapshotting local environment into Approved DB...")
    conn = init_db()
    cur = conn.cursor()
    count = 0

    # 1. Scan Python (requirements.txt)
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r") as f:
            for line in f:
                if "==" in line and not line.strip().startswith("#"):
                    try:
                        # Split "flask==2.0.1" -> pkg="flask", ver="2.0.1"
                        pkg, ver = line.split("#")[0].strip().split("==", 1)
                        cur.execute("INSERT OR IGNORE INTO approved_versions VALUES (?, ?, ?)", 
                                  ("pypi", pkg.strip(), ver.strip()))
                        count += 1
                    except ValueError:
                        pass

    # 2. Scan Node (package.json)
    if os.path.exists("package.json"):
        try:
            with open("package.json", "r") as f:
                data = json.load(f)
            # Combine dependencies and devDependencies
            deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
            for pkg, ver in deps.items():
                # Strip ^ and ~ for strict locking
                clean_ver = ver.replace("^", "").replace("~", "")
                cur.execute("INSERT OR IGNORE INTO approved_versions VALUES (?, ?, ?)", 
                          ("npm", pkg, clean_ver))
                count += 1
        except json.JSONDecodeError:
            print("⚠️ Warning: Could not parse package.json")

    conn.commit()
    conn.close()
    print(f"✅ Database updated with {count} approved dependencies.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "snapshot":
        snapshot_local()
    else:
        print("Usage: python3 adb_tool.py snapshot")
