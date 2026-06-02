# ==========================================
# utils/md_cleaner.py
# ==========================================
# RESPONSIBILITY:
#   - Post-process raw Markdown strings from any converter
#   - Normalize whitespace, remove junk lines, ensure clean output
#
# LIBRARIES: re (stdlib only)
#
# YOUR TASKS:
#   1. Strip trailing whitespace from every line
#   2. Collapse 3+ consecutive blank lines into exactly 2
#   3. Remove lines that are ONLY dashes/underscores (PDF artifacts)
#   4. Ensure file ends with exactly one newline
# ==========================================

import re


def clean_markdown(text: str) -> str:
  lines = text.splitlines()
  lines = [ line.rstrip() for line in lines]
  cleaned = "\n".join(lines)
  cleaned = re.sub(r'^[-_]{3,}$', '', cleaned, flags=re.MULTILINE)
  cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
  cleaned = cleaned.rstrip() + '\n'
  return  cleaned