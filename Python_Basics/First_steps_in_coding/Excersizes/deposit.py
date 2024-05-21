deposit = float(input())
period = int(input())
interest = float(input())

total = deposit+period*((deposit*interest/100)/12)

print(total)

