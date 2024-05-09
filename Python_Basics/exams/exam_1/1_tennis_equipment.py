from math import ceil,floor

racquet_price = float(input())
racquet_pcs = int(input())
sneakers_pcs = int(input())

sneakers_price = racquet_price / 6

total_price = (racquet_pcs * racquet_price + sneakers_pcs * sneakers_price) * 1.2

print(f'Price to be paid by Djokovic {floor(total_price / 8)}')
print(f'Price to be paid by sponsors {ceil(total_price * 7 / 8)}')
