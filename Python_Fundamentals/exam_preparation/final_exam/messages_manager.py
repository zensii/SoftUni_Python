def add(command, record):
    _, username, sent, received = command
    sent, received = int(sent), int(received)
    if username not in record:
        record[username] = {'sent': sent, 'received': received}
    return record


def message(command, record):
    _, sender, receiver = command
    if sender in record and receiver in record:
        record[sender]['sent'] += 1
        record = check_capacity(sender, capacity, record)
        record[receiver]['received'] += 1
        record = check_capacity(receiver, capacity, record)
    return record


def empty(command, record):
    username = command[1]
    if username == 'All':
        record = {}
    elif username in record:
        del record[username]

    return record


def check_capacity(username, capacity, record):

    if record[username]['sent'] + record[username]['received'] >= capacity:
        del record[username]
        print(f"{username} reached the capacity!")
    return record


capacity = int(input())
record = {}

while True:
    line = input()
    if line == 'Statistics':
        break
    command = line.split('=')

    if command[0] == 'Add':
        record = add(command, record)
    elif command[0] == 'Message':
        record = message(command, record)
    elif command[0] == 'Empty':
        record = empty(command, record)

print(f"Users count: {len(record.keys())}")
for user, statistics in record.items():
    print(f"{user} - {sum(statistics.values())}")
