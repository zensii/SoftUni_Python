key = int(input())
entries = int(input())
message = ''

for entry in range(entries):
    symbol = ord(input()) + key
    message += chr(symbol)

print(message)
