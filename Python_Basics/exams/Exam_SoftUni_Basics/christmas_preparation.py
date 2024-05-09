paper_rolls = int(input())
rolls_fabric = int(input())
glue_liters = float(input())
discount = int(input())

price_paper = 5.8
price_fabric = 7.2
price_glue = 1.2

total = price_paper * paper_rolls + price_fabric * rolls_fabric + price_glue * glue_liters
bill = total - (total * (discount / 100))
print(f'{bill:.3f}')
