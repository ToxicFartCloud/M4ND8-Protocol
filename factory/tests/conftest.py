# tests/conftest.py
import pytest
import yaml
import os
from pathlib import Path

# --- CONFIGURATION ---
MANIFEST_PATH = Path("manifest.yaml")  # Root manifest
TIER_HIERARCHY = {
    "micro_mvp": 1,
    "professional": 2,
    "enterprise": 3
}

def get_current_tier():
    """
    Reads the 'runtime_tier' from manifest.yaml.
    Defaults to 'enterprise' (run everything) if not found, to be safe.
    """
    if not MANIFEST_PATH.exists():
        # Fallback for CI or incomplete scaffolds
        return os.getenv("TARGET_BUILD_TIER", "enterprise")
    
    try:
        with open(MANIFEST_PATH, "r") as f:
            data = yaml.safe_load(f)
            # Support both 'runtime_tier' (manifesto) and 'target_build_tier' (spec) keys
            return data.get("runtime_tier") or data.get("target_build_tier", "enterprise")
    except Exception:
        return "enterprise"

# Cache the tier at startup so we don't read the file for every test function
CURRENT_TIER_NAME = get_current_tier()
CURRENT_TIER_LEVEL = TIER_HIERARCHY.get(CURRENT_TIER_NAME, 3)

def pytest_configure(config):
    """
    Register the custom markers so pytest doesn't warn about 'unknown marker'.
    """
    config.addinivalue_line("markers", "tier(name): mark test to run only on this tier or higher")
    config.addinivalue_line("markers", "micro_mvp: mark test for Core/MicroMVP tier")
    config.addinivalue_line("markers", "professional: mark test for Professional tier")
    config.addinivalue_line("markers", "enterprise: mark test for Enterprise tier")

def pytest_runtest_setup(item):
    """
    The Gatekeeper: Before any test runs, check its tier marker.
    """
    # 1. Check for specific tier markers
    required_level = 0
    tier_name = ""

    # Check for @pytest.mark.tier("enterprise")
    tier_marker = item.get_closest_marker("tier")
    if tier_marker:
        tier_name = tier_marker.args[0]
        required_level = TIER_HIERARCHY.get(tier_name, 3)
    
    # Check for shortcut markers like @pytest.mark.enterprise
    for t, level in TIER_HIERARCHY.items():
        if item.get_closest_marker(t):
            required_level = level
            tier_name = t
            break

    # 2. The Decision Logic (Subtractive)
    # If the test requires a higher level than the current build, SKIP it.
    if required_level > CURRENT_TIER_LEVEL:
        pytest.skip(
            f"DORMANT PROTOCOL: Test requires '{tier_name}' (L{required_level}), "
            f"but current build is '{CURRENT_TIER_NAME}' (L{CURRENT_TIER_LEVEL})."
        )
