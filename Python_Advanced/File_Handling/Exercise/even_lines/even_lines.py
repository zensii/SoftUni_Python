to_replace = ["-", ",", ".", "!", "?"]

""" original text here:
-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.
"""

with open("text.txt", "r+") as text:
    lines = text.readlines()
    text.seek(0)
    reversed_text = []

    for index, line in enumerate(lines):
        if index % 2 == 0:
            line = ''.join(map(lambda x: x if x not in to_replace else '@', line))
            reversed_line = ' '.join(reversed(line.split()))
            reversed_text.append(reversed_line)
    text.write('\n'.join(reversed_text))
    text.truncate()




