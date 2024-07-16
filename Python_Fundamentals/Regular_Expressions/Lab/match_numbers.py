import re

string = input()
# regex = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
regex = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)\.?\d*($|(?=\s))'

matches = re.finditer(regex, string)

for match in matches:
    print(match.group(), end=' ')
