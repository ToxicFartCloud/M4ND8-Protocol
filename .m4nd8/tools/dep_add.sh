#!/usr/bin/env bash
# .m4nd8/tools/dep_add.sh
# Usage: ./dep_add.sh python package==version
#        ./dep_add.sh system package==version

ECOSYSTEM=$1
PACKAGE_SPEC=$2

if [[ -z "$ECOSYSTEM" || -z "$PACKAGE_SPEC" ]]; then
    echo "Usage: $0 <ecosystem> <package==version>"
    echo "Example: $0 python customtkinter==5.2.2"
    exit 1
fi

# Add to approved dependencies
jq --arg eco "$ECOSYSTEM" --arg pkg_spec "$PACKAGE_SPEC" \
   '.[$eco] += {($pkg_spec | split("==")[0]): ($pkg_spec | split("==")[1])}' \
   factory/data/approved_dependencies.json > temp.json && mv temp.json factory/data/approved_dependencies.json

echo "✅ Added $PACKAGE_SPEC to approved dependencies"
echo "🔄 Run ./pack_protocol.sh to update distribution"
