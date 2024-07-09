class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


usr_input = input()
info = []

while usr_input != 'Stop':
    info.append(usr_input)
    usr_input = input()

sent_mails = [int(num) for num in input().split(', ')]

for number, mail in enumerate(info):
    mail_data = mail.split()
    email = Email(mail_data[0], mail_data[1], mail_data[2])
    if number in sent_mails:
        email.send()
    print(email.get_info())
