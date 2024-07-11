path = input()

extension = path.split('.')[1]
name = path.split('.')[0].split('\\')[-1]

print(f'File name: {name}')
print(f'File extension: {extension}')
