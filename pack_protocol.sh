#!/bin/bash
# pack_protocol.sh — Sync Factory to Distribution
# Purpose: Build the .m4nd8/ distribution artifact from the factory/ source.

set -euo pipefail

FACTORY="factory"
DIST=".m4nd8"

echo "📦 Packing M4ND8 Protocol..."

# 1. Sync Kernel (Identity & Handbook)
# Added handbook to the sync list
cp "$FACTORY/kernel/director.yaml" "$DIST/"
cp "$FACTORY/kernel/manifesto.md" "$DIST/"
cp "$FACTORY/kernel/M4ND8_handbook.md" "$DIST/"

# 2. Sync Runtime Tools & Binaries
mkdir -p "$DIST/tools" "$DIST/bin"
cp -r "$FACTORY/runtime/tools/"* "$DIST/tools/"
# Fixed: Explicitly copy contents of bin to .m4nd8/bin
cp -r "$FACTORY/runtime/bin/"* "$DIST/bin/"

# 3. Sync Data
mkdir -p "$DIST/data"
cp -r "$FACTORY/data/"* "$DIST/data/"

# 4. Sync Policies
mkdir -p "$DIST/policies" "$DIST/policy"
cp -r "$FACTORY/source_policies/policies/"* "$DIST/policies/"
cp -r "$FACTORY/source_policies/policy/"* "$DIST/policy/"

# 5. Sync Templates & Interface Docs
mkdir -p "$DIST/templates"
cp -r "$FACTORY/interface/templates/"* "$DIST/templates/"
# Added: Sync onboarding files from interface root
cp "$FACTORY/interface/onboarding.md" "$DIST/" 2>/dev/null || true
cp "$FACTORY/interface/onboarding.png" "$DIST/" 2>/dev/null || true

# Ensure all scripts are executable in the distribution
chmod +x "$DIST/bin/"*
chmod +x "$DIST/tools/"*.sh 2>/dev/null || true

echo "✅ Protocol Packed. All handbook and bin files included."
