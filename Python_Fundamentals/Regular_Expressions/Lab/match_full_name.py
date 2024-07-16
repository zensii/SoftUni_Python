import re

string = input()
regex = r"\b[A-Z][a-z]{1,} [A-Z][a-z]{1,}\b"

matches = re.findall(regex, string)

print(' '.join(matches))
