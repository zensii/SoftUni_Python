def add(title):
    if title not in lessons:
        lessons.append(title)
    return lessons


def insert(title, index):
    if title not in lessons:
        lessons.insert(index, title)
    return lessons

def remove(title):
    if title in lessons:
        lessons.remove(title)
    if f'{title}-Exercise' in lessons:
        lessons.remove(f'{title}-Exercise')
    return lessons

def swap(title, title_new):
    if title in lessons and title_new in lessons:
        index_1 = lessons.index(title)
        index_2 = lessons.index(title_new)
        lessons[index_1], lessons[index_2] = lessons[index_2], lessons[index_1]

    if f'{title}-Exercise' in lessons and f'{title_new}-Exercise' in lessons:
        index_ex1 = lessons.index(f'{title}-Exercise')
        index_ex2 = lessons.index(f'{title_new}-Exercise')
        lessons[index_ex1], lessons[index_ex2] = \
            lessons[index_ex2], lessons[index_ex1]

    elif f'{title}-Exercise' in lessons:
        lessons.insert(lessons.index(title)+1, lessons.pop(lessons.index(f'{title}-Exercise')))
    elif f'{title_new}-Exercise' in lessons:
        lessons.insert(lessons.index(title_new)+1, lessons.pop(lessons.index(f'{title_new}-Exercise')))

    return lessons

def exercise(title):
    if title in lessons and f'{title}-Exercise' not in lessons:
        lessons.insert(lessons.index(title)+1, f'{title}-Exercise')
    elif title not in lessons and f'{title}-Exercise' not in lessons:
        lessons.append(title)
        lessons.append(f'{title}-Exercise')




lessons = input().split(', ')
while True:
    usr_input = input().split(':')
    command = usr_input[0]
    if len(usr_input) > 1:
        title = usr_input[1]
    if len(usr_input) > 2:
        title_new = index = usr_input[2]

    if command == 'course start':
        break

    elif command == 'Add':
        add(title)
    elif command == 'Insert':
        insert(title, int(index))
    elif command == 'Remove':
        remove(title)
    elif command == 'Swap':
        swap(title, title_new)
    elif command == 'Exercise':
        exercise(title)

for index, course in enumerate(lessons):
    print(f'{index+1}.{course}')
