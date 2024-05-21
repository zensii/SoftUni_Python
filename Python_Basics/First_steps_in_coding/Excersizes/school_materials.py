pens = int(input())
markers = int(input())
cleaner = int(input())
discount = int(input())

pen_price = 5.8
marker_price = 7.2
cleaner_price = 1.2

total = pens*pen_price + markers*marker_price + cleaner*cleaner_price
discounted_total = total-(total*(discount/100))

print(discounted_total)


