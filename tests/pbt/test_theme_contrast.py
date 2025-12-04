"""
Property-Based Test for WCAG 2.2 AA Contrast (4.5:1)
Validates all foreground/background pairs in src/theme/tokens.json.
"""
import json
import os
from hypothesis import given, strategies as st

def rgb_to_luminance(r, g, b):
    """Convert RGB to relative luminance (WCAG formula)."""
    def _adjust(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * _adjust(r) + 0.7152 * _adjust(g) + 0.0722 * _adjust(b)

def contrast_ratio(bg, fg):
    """Calculate contrast ratio between two RGB tuples."""
    l1 = rgb_to_luminance(*bg)
    l2 = rgb_to_luminance(*fg)
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)

def load_tokens():
    with open("src/theme/tokens.json") as f:
        return json.load(f)

tokens = load_tokens()
colors = {}
for mode in ["light_mode", "dark_mode"]:
    for k, v in tokens["colors"][mode].items():
        if k == "contrast_ratio_min":
            continue
        # Convert hex to RGB
        hex_v = v.lstrip("#")
        rgb = tuple(int(hex_v[i:i+2], 16) for i in (0, 2, 4))
        colors[f"{mode}_{k}"] = rgb

color_names = list(colors.keys())
rgb_values = list(colors.values())

@given(
    bg_idx=st.integers(min_value=0, max_value=len(color_names)-1),
    fg_idx=st.integers(min_value=0, max_value=len(color_names)-1)
)
def test_contrast(bg_idx, fg_idx):
    bg_name = color_names[bg_idx]
    fg_name = color_names[fg_idx]
    # Skip if both are background or both are text
    if ("background" in bg_name and "background" in fg_name) or \
       ("text" not in bg_name and "text" not in fg_name):
        return
    bg_rgb = rgb_values[bg_idx]
    fg_rgb = rgb_values[fg_idx]
    ratio = contrast_ratio(bg_rgb, fg_rgb)
    assert ratio >= 4.5, f"Contrast failed: {bg_name} vs {fg_name} = {ratio:.2f}"
