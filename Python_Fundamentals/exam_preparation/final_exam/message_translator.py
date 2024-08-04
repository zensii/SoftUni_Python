import re


regex = r'!([A-Z][a-z]{2,})!:\[([a-zA-Z]{8,})\]'

n = int(input())
inputs = []
for _ in range(n):
    inputs.append(input())

for inpt in inputs:
    result = re.findall(regex, inpt)

    if result:
        command, message = re.findall(regex, inpt)[0]
        translated_message = [str(ord(char)) for char in message]

        print(f"{command}: {' '.join(translated_message)}")
    else:
        print(f"The message is invalid")
