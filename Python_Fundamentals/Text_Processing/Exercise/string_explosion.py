chain = input()
result_string = ''
index = 0
strength = 0
while index < len(chain):
    if chain[index] != '>':
        result_string += chain[index]
        index += 1
    elif chain[index] == '>':
        result_string += '>'
        index += 1
        strength += int(chain[index])
        for i in range(1, strength+1):
            if index < len(chain) and chain[index] != '>':
                index += 1
                strength -= 1
            else:
                break

print(result_string)
