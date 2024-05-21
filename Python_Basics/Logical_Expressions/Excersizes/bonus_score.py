a = int(input())

bonus = 0
extra_bonus = 0

if a <= 100:
    bonus = 5
elif 100 < a <= 1000:
    bonus = a * 0.2
elif a > 1000:
    bonus = a * 0.1

if a % 2 == 0:
    extra_bonus = 1
elif a % 5 == 0:
    extra_bonus = 2

print(bonus + extra_bonus)
print(bonus + extra_bonus + a)
