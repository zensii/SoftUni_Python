import re

with open("words.txt") as words, open("input.txt") as text:
    words = words.read().split()
    text = text.read()

with open("output.txt", 'w') as output:
    counted = []

    for word in words:
        matches = re.findall(fr"\W{word}\W", text, re.IGNORECASE)
        counted.append((word, len(matches)))

    for counts in sorted(counted, key=lambda x: -x[1]):
        output.write(f"{counts[0]} - {counts[1]}\n")
