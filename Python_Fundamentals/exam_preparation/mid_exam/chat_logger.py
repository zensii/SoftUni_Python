def edit(old_msg, new_msg, log):
    if old_msg in log:
        log.insert(log.index(old_msg), new_msg)
        log.remove(old_msg)
    return log


def pin(msg, log):
    if msg in log:
        log.append(msg)
        log.remove(msg)
    return log


def spam(spam_list, log):
    for msg in spam_list:
        log.append(msg)
    return log


chat_log = []

while True:

    command = input()

    if command == 'end':
        break

    chat_actions = command.split()

    cmd_type = chat_actions[0]

    if cmd_type == 'Chat':
        message = chat_actions[1]
        chat_log.append(message)

    if cmd_type == 'Delete':
        message = chat_actions[1]
        if message in chat_log:
            chat_log.remove(message)

    if cmd_type == 'Edit':
        old_message = chat_actions[1]
        edited_msg = chat_actions[2]
        chat_log = edit(old_message, edited_msg, chat_log)

    if cmd_type == 'Pin':
        message = chat_actions[1]
        chat_log = pin(message, chat_log)

    if cmd_type == 'Spam':
        spam_list = chat_actions[1:]
        chat_log = spam(spam_list, chat_log)

for message in chat_log:
    print(message)
