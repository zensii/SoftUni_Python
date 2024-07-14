string = input()
decoded = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
message = ''
for char in string:
    if ord(char) in decoded.keys():
        message += chr(decoded[ord(char)])
    else:
        message += char
print(message)
#
#
# decoded = ''
# string = input()
# for char in string:
#     if char.isalpha():
#         if ord(char) <= 120:
#             decoded += (chr(ord(char)+2))
#         elif ord(char) == 121:
#             decoded += chr(97)
#         elif ord(char) == 122:
#             decoded += chr(98)
#     else:
#         decoded += char
#
# print(decoded)
