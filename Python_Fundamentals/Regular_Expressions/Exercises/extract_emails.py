import re

string = input()
regex = r'\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'

matches = re.finditer(regex, string)

for match in matches:

    print(match.group())
