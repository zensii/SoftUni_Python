numbers = input().split()
inverted_lst = []
for number in numbers:
    if int(number) >= 0:
        inverted_lst.append(int(number)-2*int(number))
    else:
        inverted_lst.append(int(number)+2*abs(int(number)))

print(inverted_lst)