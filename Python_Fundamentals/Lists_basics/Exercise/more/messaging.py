key_sequence = input().split(' ')
key_message = list(input())
code_keys = []
decoded_message = ''
for keys in key_sequence:
    key = sum(int(digit) for digit in keys)
    decoded_message += key_message.pop(key % len(key_message))
print(decoded_message)
