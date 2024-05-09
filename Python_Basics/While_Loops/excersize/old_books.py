target_book = input()
current_book = input()
counter = 0

while current_book != target_book:

    if current_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {counter} books.')
        break
    counter += 1
    current_book = input()
else:
    print(f'You checked {counter} books and found it.')



