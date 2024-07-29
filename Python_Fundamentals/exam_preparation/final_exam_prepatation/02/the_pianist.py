def add(pieces, *args):
    _, piece, composer, key = args
    if piece not in pieces:
        pieces[piece] = {'Composer': composer, 'Key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f'{piece} is already in the collection!')
    return pieces


def remove(pieces, *args):
    _, piece = args
    if piece in pieces:
        del pieces[piece]
        print(f'Successfully removed {piece}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    return pieces


def change_key(pieces, *args):
    _, piece, new_key = args
    if piece in pieces:
        pieces[piece]['Key'] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces


def main():
    pieces = {}
    n = int(input())
    for musical_piece in range(n):
        piece, composer, key = input().split('|')
        pieces[piece] = {'Composer': composer, 'Key': key}

    usr_input = input()
    while usr_input != 'Stop':
        command = usr_input.split('|')
        if command[0] == 'Add':
            pieces = add(pieces, *command)
        elif command[0] == 'Remove':
            pieces = remove(pieces, *command)
        elif command[0] == 'ChangeKey':
            pieces = change_key(pieces, *command)
        usr_input = input()

    for piece, piece_info in pieces.items():
        composer = piece_info['Composer']
        key = piece_info['Key']
        print(f'{piece} -> Composer: {composer}, Key: {key}')


if __name__ == '__main__':
    main()