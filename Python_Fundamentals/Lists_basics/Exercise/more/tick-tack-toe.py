first_line = input().split()
second_line = input().split()
third_line = input().split()


for x in range(3):
    if (first_line[x]+second_line[x]+third_line[x]) == '111':
        print('First player won')
        break
    elif (first_line[0]+second_line[1]+third_line[2]) == '111':
        print('First player won')
        break
    elif (first_line[2]+second_line[1]+third_line[0]) == '111':
        print('First player won')
        break
    elif ''.join(first_line) == '111' or ''.join(second_line) == '111' or ''.join(third_line) == '111':
        print('First player won')
        break
    elif (first_line[x]+second_line[x]+third_line[x]) == '222':
        print('Second player won')
        break
    elif (first_line[0]+second_line[1]+third_line[2]) == '222':
        print('Second player won')
        break
    elif (first_line[2]+second_line[1]+third_line[0]) == '222':
        print('Second player won')
        break
    elif ''.join(first_line) == '222' or ''.join(second_line) == '222' or ''.join(third_line) == '222':
        print('Second player won')
        break

else:
    print('Draw!')
