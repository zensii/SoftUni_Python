n = int(input())
keyword = input()
lst = []
trimmed_lst =[]

for entry in range(n):
    string = input()
    lst.append(string)

print(lst)

for string in lst:
    words = string.split()
    if keyword in words:
        trimmed_lst.append(string)

print(trimmed_lst)
