#!/bin/bash
# pack_protocol.sh — Sync Factory to Distribution
# Purpose: Build the .m4nd8/ distribution artifact from the factory/ source.

set -euo pipefail

FACTORY="factory"
DIST=".m4nd8"
MANIFEST="$DIST/MANIFEST"

echo "📦 Packing M4ND8 Protocol..."

# 1. Sync Kernel (Identity)
# director.yaml, manifesto.md go to root of .m4nd8
cp "$FACTORY/kernel/director.yaml" "$DIST/"
cp "$FACTORY/kernel/manifesto.md" "$DIST/"

# 2. Sync Runtime Tools
# Copy tools/ to .m4nd8/tools/
mkdir -p "$DIST/tools"
cp -r "$FACTORY/runtime/tools/"* "$DIST/tools/"
cp -r "$FACTORY/runtime/bin/"* "$DIST/bin/" 2>/dev/null || true

# 3. Sync Data
mkdir -p "$DIST/data"
cp -r "$FACTORY/data/"* "$DIST/data/"

# 4. Sync Policies
# Mirror structure for backward compatibility
mkdir -p "$DIST/policies" "$DIST/policy"
cp -r "$FACTORY/source_policies/policies/"* "$DIST/policies/"
cp -r "$FACTORY/source_policies/policy/"* "$DIST/policy/"

# 5. Sync Templates
mkdir -p "$DIST/templates"
cp -r "$FACTORY/interface/templates/"* "$DIST/templates/"

# 6. Generate Manifest
echo "📜 Generating MANIFEST..."
rm -f "$MANIFEST"
find "$DIST" -type f -not -name "MANIFEST" | sort | while read -r file; do
    sha256sum "$file" >> "$MANIFEST"
done

echo "✅ Protocol Packed. Manifest updated."
