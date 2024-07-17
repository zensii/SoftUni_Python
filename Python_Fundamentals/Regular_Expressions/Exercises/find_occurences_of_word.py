import re

string = input()
word = input()

counter = 0

regex = re.compile(fr'\b{word}\b', re.IGNORECASE)

matches = re.findall(regex, string)
print(len(matches))