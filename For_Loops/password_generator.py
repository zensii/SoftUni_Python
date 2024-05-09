import random
from string import ascii_letters, digits, punctuation

# Combine all characters sets
all_characters = ascii_letters + digits + punctuation

password_length = 12

password = ''.join(random.sample(all_characters, password_length))

print(password)


