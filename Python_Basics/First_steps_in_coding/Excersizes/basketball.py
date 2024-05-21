subscription = int(input())

shoes = subscription - subscription*0.4
suit = shoes - shoes*0.2
ball = suit/4
accessories = ball/5

total_cost = subscription + shoes + suit + ball + accessories

print(f'{total_cost:.2f}')
