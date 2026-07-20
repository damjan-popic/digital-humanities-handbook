#!/usr/bin/env bash
set -euo pipefail

OWNER="${1:-damjan-popic}"
REPO="${2:-digital-humanities-handbook}"
FULL="$OWNER/$REPO"

command -v gh >/dev/null 2>&1 || {
  echo "GitHub CLI (gh) is required: https://cli.github.com/" >&2
  exit 1
}
gh auth status >/dev/null

if git remote get-url origin >/dev/null 2>&1; then
  echo "Refusing to replace existing origin: $(git remote get-url origin)" >&2
  exit 1
fi

make check

gh repo view "$FULL" >/dev/null 2>&1 && {
  echo "Repository $FULL already exists. Add it as origin manually after checking its contents." >&2
  exit 1
}

gh repo create "$FULL" \
  --public \
  --source=. \
  --remote=origin \
  --push \
  --description="Open, bilingual and versioned handbook for digital humanities methods" \
  --homepage="https://${OWNER}.github.io/${REPO}/"

gh repo edit "$FULL" \
  --enable-issues=true \
  --enable-discussions=true \
  --add-topic digital-humanities \
  --add-topic open-education \
  --add-topic mkdocs \
  --add-topic slovenian \
  --add-topic text-analysis \
  --add-topic corpus-linguistics

echo "Created and pushed https://github.com/$FULL"
echo "In Settings → Pages, confirm GitHub Actions as the deployment source."
