import re

string = input()
mirror_words = []
regex = r'([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

results = re.findall(regex, string)

if not results:
    print("No word pairs found!")
else:
    print(f"{len(results)} word pairs found!")

    for result in results:
        word1, word2 = result[1], result[2]

        if word1 == word2[::-1]:
            mirror_words.append(word1 + ' <=> ' + word2)
if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(mirror_words))

