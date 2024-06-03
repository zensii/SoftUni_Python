input_string = ['abcdef6', ' asdafafa']
parts = 4

new_list = []

if len(input_string[0]) % parts == 0:
    for i in range(0, len(input_string[0]), len(input_string[0])//parts):
        new_list.append(input_string[0][i:i+parts])
else:
    for i in range(0, len(input_string[0])//parts, len(input_string[0])//parts):
        new_list.append(input_string[0][i:i+parts])
    new_list.append(input_string[0][(len(new_list)*parts):])
    input_string[0] = new_list

print(input_string)