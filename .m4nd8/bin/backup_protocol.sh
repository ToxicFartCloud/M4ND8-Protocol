#!/bin/bash
# backup_protocol.sh
# Purpose: Create a timestamped backup of the factory and distribution.

set -e

BACKUP_DIR=".backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
ARCHIVE="$BACKUP_DIR/m4nd8_backup_$TIMESTAMP.tar.gz"

mkdir -p "$BACKUP_DIR"

echo "💾 Backing up M4ND8 Protocol to $ARCHIVE..."
tar --exclude='./.git' --exclude='./_logs' --exclude='./.backups' -czf "$ARCHIVE" .

echo "✅ Backup complete."
