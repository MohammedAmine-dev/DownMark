
import re


def clean_markdown(text: str) -> str:
  lines = text.splitlines()
  lines = [ line.rstrip() for line in lines]
  cleaned = "\n".join(lines)
  cleaned = re.sub(r'^[-_]{3,}$', '', cleaned, flags=re.MULTILINE)
  cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
  cleaned = cleaned.rstrip() + '\n'
  return  cleaned