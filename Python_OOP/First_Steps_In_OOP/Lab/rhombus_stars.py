def print_line(spaces, stars):
    return f"{spaces * ' '}{stars * '* '}"

def print_rhombus(n):
    for i in range(1, n+1):
        spaces = n - i
        stars = i
        print(print_line(spaces, stars))
    for i in range(n-1, -1, -1):
        spaces = n - i
        stars = i
        print(print_line(spaces, stars))

print_rhombus(int(input()))