def words_sorting(*words):
    my_d = {}
    for word in words:
        my_d[word] = sum([ord(char) for char in word])

    result = ''
    for key, value in sorted(my_d.items(), key=lambda x: -x[1] if sum(my_d.values()) % 2 != 0 else x[0]):
        result += f"{key} - {value}\n"

    return result

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
