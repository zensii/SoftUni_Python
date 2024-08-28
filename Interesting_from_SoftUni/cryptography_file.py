from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

encrypt_token = f.encrypt(b'Svetlin Ivanov IBAN: 123456789')
print(encrypt_token)

decrypt_token = f.decrypt(encrypt_token)
print(decrypt_token)


# може да се направи софтуер (конзолка например) която декриптира изпратения енкрипт токен