orders = int(input())
total_price = 0

for order in range(orders):

    price = float(input())
    days = int(input())
    consumption = int(input())

    if not 0.01 <= price <= 100.00:
        continue
    if not 1 <= days <= 31:
        continue
    if not 1 <= consumption <= 2000:
        continue

    order_price = price * days * consumption

    print(f'The price for the coffee is: ${order_price:.2f}')
    total_price += order_price

print(f'Total: ${total_price:.2f}')
