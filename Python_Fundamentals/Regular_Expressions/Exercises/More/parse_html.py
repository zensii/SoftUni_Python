import re

raw = input()

title_regex = r'<title>(.*)<\/title>'
content_regex = r'<body>(.*?)<\/body>'

title = re.findall(title_regex, raw, re.DOTALL)[0]
body = re.findall(content_regex, raw, re.DOTALL)[0]

content = re.sub(r'(<.*?>)|(\\n)', '', body)

print(f'Title: {title}')
print(f'Content: {content}')
