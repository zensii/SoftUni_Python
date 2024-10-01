with open('text.txt') as text:
    lines = text.readlines()

new_text = []

for index, line in enumerate(lines):
    line = line.rstrip()
    letters = len([char for char in line if char.isalnum()])
    spaces = len([char for char in line if char.isspace()])
    punctuation = len(line) - letters - spaces
    new_text.append(f"Line {index+1}: {line} ({letters})({punctuation})")

with open('processed_text.txt', "w") as text:
    new_text = '\n'.join(new_text)
    text.write(new_text)
