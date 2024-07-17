import re

regex = r'\d+'
matches = []
usr_input = input()
while usr_input:
    match = re.findall(regex, usr_input)
    if match:
        print(' '.join(match), end=' ')
    usr_input = input()


