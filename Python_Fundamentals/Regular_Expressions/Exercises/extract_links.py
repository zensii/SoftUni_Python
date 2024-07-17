import re

string = input()

regex = r'(?:www).(?:[a-zA-Z0-9\-]+)(?:\.[a-z]+)+'

while string:

    match = re.findall(regex, string)
    if match:
        print(''.join(match))

    string = input()
