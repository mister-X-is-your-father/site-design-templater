#!/bin/bash
#
# Fetch a reference site HTML for analysis
#
# Usage:
#   ./fetch-site.sh <url> [output_file]
#
# Examples:
#   ./fetch-site.sh https://ishikawakazuya.net
#   ./fetch-site.sh https://example.com /tmp/example.html

set -e

URL="${1:?Usage: $0 <url> [output_file]}"
OUTPUT="${2:-/tmp/$(echo "$URL" | sed 's|https\?://||; s|/.*||').html}"

echo "Fetching: $URL"
echo "Output: $OUTPUT"

# Fetch with timeout and user agent
curl -L \
    --max-time 30 \
    --user-agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
    -o "$OUTPUT" \
    "$URL"

if [ -f "$OUTPUT" ]; then
    SIZE=$(wc -c < "$OUTPUT")
    echo "Success: Downloaded $SIZE bytes"
    echo ""
    echo "To analyze structure:"
    echo "  grep -oP '<[a-z]+[^>]*class=\"[^\"]*\"' $OUTPUT | head -50"
else
    echo "Failed to download"
    exit 1
fi
