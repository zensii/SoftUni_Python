males = int(input())
females = int(input())
tables = int(input())
full = False

for man in range(1, males+1):
    for woman in range(1, females+1):
        tables -= 1
        print(f'({man} <-> {woman})', end=' ')
        if tables == 0:
            full = True
            break
    if full:
        break
