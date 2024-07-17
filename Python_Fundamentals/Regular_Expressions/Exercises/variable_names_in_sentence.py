import re

string = input()

regex = r"(?<= _)[A-Za-z\d]+\b"

matches = re.findall(regex, string)

print(','.join(matches))
