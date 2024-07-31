import re
from functools import reduce
emojis_regex = r'([:*])\1[A-Z][a-z]{2,}\1\1'

string = input()

emojis = [emoji[0] for emoji in re.finditer(emojis_regex, string)]

coolness_threshold = reduce((lambda x, y: x * y), [int(digit) for digit in re.findall(r'\d', string)])

print(f"Cool threshold: {coolness_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")

for emoji in emojis:
    if sum([ord(char) for char in emoji if char != '*' and char != ':']) > coolness_threshold:
        print(emoji)

