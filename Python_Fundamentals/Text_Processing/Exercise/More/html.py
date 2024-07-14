def convert(title, content, comments):
    print(f'<h1>\n    {title}\n</h1>')
    print(f'<article>\n    {content}\n</article>')
    for comment in comments:
        print(f'<div>\n    {comment}\n</div>')


title = input()
content = input()
usr_input = input()
comments = []

while usr_input != 'end of comments':
    comments.append(usr_input)
    usr_input = input()

convert(title, content, comments)
