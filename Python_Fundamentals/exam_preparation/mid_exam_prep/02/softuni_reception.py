import math

eff_1 = int(input())
eff_2 = int(input())
eff_3 = int(input())
students = int(input())
worked_hours = 0
worked_no_brake = 0

while students > 0:

    students -= eff_1 + eff_2 + eff_3
    worked_hours += 1
    worked_no_brake += 1

    if worked_no_brake == 3 and students > 0:
        worked_hours += 1  # 1 hour brake
        worked_no_brake = 0

print(f"Time needed: {worked_hours:.0f}h.")
