import re

string = input()
regex = r"(\+359([ -])2\2\d{3}\2\d{4})\b"


matches = re.findall(regex, string)

phones = [matches[0] for matches in re.findall(regex, string)]
print(', '.join(phones))

