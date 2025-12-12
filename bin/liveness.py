# diagnostic/liveness_checker.py
import requests
import subprocess
import time
from typing import Dict, Any

def check_backend_liveness(config: Dict[str, Any]) -> Dict[str, Any]:
    """Verify the REAL backend is running, not a mock."""
    expected_port = config.get("backend_port", 8000)
    health_endpoint = config.get("health_endpoint", "/health")
    process_name = config.get("expected_process", "uvicorn")  # or gunicorn, etc.

    # 1. Check process existence
    result = subprocess.run(
        ["pgrep", "-f", process_name],
        capture_output=True,
        text=True
    )
    process_exists = len(result.stdout.strip()) > 0

    # 2. Check HTTP liveness
    try:
        resp = requests.get(f"http://localhost:{expected_port}{health_endpoint}", timeout=2)
        http_healthy = resp.status_code == 200 and "mock" not in resp.text.lower()
    except requests.RequestException:
        http_healthy = False

    return {
        "process_exists": process_exists,
        "http_healthy": http_healthy,
        "is_mock": "mock" in (resp.text if not isinstance(resp, bool) else "").lower(),
        "score": int(process_exists) + int(http_healthy) - int("mock" in (resp.text if not isinstance(resp, bool) else ""))
    }

# Usage in fnl_chk.yaml verification script
if __name__ == "__main__":
    import yaml, sys
    with open("manifest.yaml") as f:
        manifest = yaml.safe_load(f)
    result = check_backend_liveness(manifest.get("backend", {}))
    if result["score"] < 2:
        print(f"FAIL: Backend liveness check failed. Mock detected: {result['is_mock']}")
        sys.exit(1)
    else:
        print("PASS: Real backend confirmed running.")
