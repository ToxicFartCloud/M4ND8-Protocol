#!/usr/bin/env python3
"""
update_adb.py — Approved Dependency Base Updater
Purpose: Pull a public table of approved dependencies and generate .m4nd8/data/approved_dependencies.db
Usage: python update_adb.py
Output: .m4nd8/data/approved_dependencies.db (SQLite)
Note: This script is for protocol maintainers only. It is NOT part of the .m4nd8 capsule.
"""

import os
import sys
import sqlite3
import urllib.request
import json
from pathlib import Path

# CONFIGURATION — Replace with your own source
# Option A: Public JSON endpoint (e.g., GitHub Gist, Google Apps Script)
ADB_SOURCE_URL = "https://gist.githubusercontent.com/ToxicFartCloud/9e94ec37a63a933cd714a92e6cce13c5/raw/863876140699dbc204f1c24c3235ac16bf736ad9/gistfile1.txt"

# Option B: Local CSV/JSON path (for air-gapped or private use)
# ADB_SOURCE_PATH = "./approved_deps.json"

def fetch_approved_deps():
    """Fetch from remote JSON source."""
    print("📡 Fetching Approved Dependency Base from remote source...")
    try:
        with urllib.request.urlopen(ADB_SOURCE_URL) as resp:
            data = json.load(resp)
        return data
    except Exception as e:
        print(f"❌ Failed to fetch ADB: {e}", file=sys.stderr)
        sys.exit(1)

def ensure_data_dir():
    data_dir = Path(".m4nd8/data")
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / "approved_dependencies.db"

def init_db(db_path):
    """Initialize SQLite schema."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS approved_versions (
            ecosystem TEXT NOT NULL,
            package TEXT NOT NULL,
            version TEXT NOT NULL,
            PRIMARY KEY (ecosystem, package, version)
        )
    """)
    cur.execute("DELETE FROM approved_versions")  # Fresh update
    conn.commit()
    return conn

def main():
    deps = fetch_approved_deps()
    db_path = ensure_data_dir()
    conn = init_db(db_path)
    cur = conn.cursor()

    inserted = 0
    for eco, pkgs in deps.get("approved", {}).items():
        for pkg, versions in pkgs.items():
            if isinstance(versions, str):
                versions = [versions]
            for ver in versions:
                cur.execute(
                    "INSERT INTO approved_versions (ecosystem, package, version) VALUES (?, ?, ?)",
                    (eco, pkg, ver)
                )
                inserted += 1

    conn.commit()
    conn.close()
    print(f"✅ Wrote {inserted} approved package versions to {db_path}")

if __name__ == "__main__":
    main()
