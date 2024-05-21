hour = int(input())
minutes = int(input())

minutes = minutes + 15


if minutes / 60 >= 1:
    minutes = minutes % 60
    hour = hour + 1

if hour == 24:
    hour = 0

if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")
