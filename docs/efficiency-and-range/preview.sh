#!/usr/bin/env bash
# Rebuild the paper and its self-contained preview in one step.
#
#   ./preview.sh          build once, print the preview path
#   ./preview.sh --watch  rebuild whenever the source or the callouts change
#   ./preview.sh --open   build once and open the preview
#
# The chain has four stages and skipping any of them fails silently rather than
# loudly, which is the whole reason this script exists:
#
#   callouts.json + screenshots/raw/  --annotate.py-->  assets/images/...
#   efficiency-and-range.src.md       --render.mjs -->  efficiency-and-range.md
#   (both)                            --jekyll    -->  _site/
#   _site/                            --preview.py-->  preview.html
#
# Editing the source and forgetting to render publishes stale content with no
# error anywhere; editing callouts.json and forgetting to annotate leaves the old
# figures in place. Running all four every time costs about five seconds.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
PREVIEW="$HERE/preview.html"

build() {
  cd "$HERE"
  python3 annotate.py
  node render.mjs
  cd "$ROOT"
  bundle exec jekyll build 2>&1 | grep -E "done in|Error|error" || true
  cd "$HERE"
  python3 preview.py
  echo "--> $PREVIEW"
}

# mtimes of everything a rebuild depends on, as one string to compare against.
fingerprint() {
  stat -f '%m' "$HERE/efficiency-and-range.src.md" "$HERE/callouts.json" \
               "$ROOT/_layouts/paper.html" 2>/dev/null
  find "$HERE/screenshots/raw" -name '*.png' -exec stat -f '%m' {} + 2>/dev/null
}

case "${1:-}" in
  --watch)
    echo "watching source, callouts, layout and raw captures — ^C to stop"
    build
    last="$(fingerprint)"
    while true; do
      sleep 1
      now="$(fingerprint)"
      if [ "$now" != "$last" ]; then
        echo; echo "--- change detected, rebuilding ---"
        # Rebuild failures must not kill the watch; the next save gets a retry.
        build || echo "!!! build failed — fix and save again"
        last="$(fingerprint)"
      fi
    done
    ;;
  --open)
    build
    open "$PREVIEW"
    ;;
  *)
    build
    ;;
esac
