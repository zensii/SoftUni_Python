def search(contact):
    if contact in phonebook:
        print(f'{contact} -> {phonebook[contact]}')
    else:
        print(f'Contact {contact} does not exist.')


def add_contact(contact):
    key = contact[0]
    value = contact[1]
    phonebook[key] = value


phonebook = {}

while True:
    input_string = input()

    if input_string[0].isdigit():
        break

    contact_details = input_string.split('-')
    add_contact(contact_details)

for i in range(int(input_string)):
    contact = input()
    search(contact)
