#!/usr/bin/env bash
# Rebuild every zip in downloads/ from the current skills/ and book/ folders.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -f downloads/*.zip
for d in skills/*/; do
  n=$(basename "$d")
  (cd "$d" && zip -qr -X "../../downloads/skill-$n.zip" .)
done
(cd book && zip -q -X ../downloads/ux-research-in-the-wild-book.zip ux-research-in-the-wild.html)
(cd skills && zip -qr -X ../downloads/ux-skills-all.zip HOW-TO-USE.md PROJECT-INSTRUCTIONS.md */)
ls -1 downloads
