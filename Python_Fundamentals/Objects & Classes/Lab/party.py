class Party:
    def __init__(self):
        self.people = []


command = input()
party = Party()

while command != 'End':
    name = command
    party.people.append(name)
    command = input()

print(f"Going: {', '.join(party.people)}")
print(f'Total: {len(party.people)}')
