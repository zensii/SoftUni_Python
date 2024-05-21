a = int(input())
b = int(input())
c = int(input())

total_seconds = a + b + c

minutes = total_seconds // 60
seconds = total_seconds % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
