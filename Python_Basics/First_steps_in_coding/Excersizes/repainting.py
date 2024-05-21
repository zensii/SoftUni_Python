nylon = int(input())
paint = int(input())
thinner = int(input())
work_time = int(input())

price_nylon = 1.5
price_paint = 14.5
price_thinner = 5

total_material = ((nylon+2)*price_nylon) + (paint*price_paint*1.10) + (thinner*price_thinner) + 0.4

work_cost = total_material*0.3

total_cost = total_material+(work_cost*work_time)

print(total_cost)




