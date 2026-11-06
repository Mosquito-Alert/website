#!/usr/bin/env bash
# Rebuild the specification web page (tools/spec-build/out/) and PDF (next to the Markdown file).
# Requires: pandoc, python3, node. First run installs playwright-core; if Chromium is missing, run:
#   npx playwright-core install chromium
set -euo pipefail
cd "$(dirname "$0")"
[ -d node_modules/playwright-core ] || npm install --silent
python3 build_web.py phase1
python3 make_print.py
node make_pdf.js
