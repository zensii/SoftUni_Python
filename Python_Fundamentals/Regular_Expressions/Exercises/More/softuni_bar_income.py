import re
regex = r'%(?P<customer_name>[A-Z][a-z]+)%[^|$%\.]*<(?P<product>\w+)>[^|$%\.]*\|[^|$%\.0-9]*(?P<count>\d+)[^|$%\.0-9]*\|[^|$%\.0-9]*(?P<price>[\d]+[\.\d]*)[^|$%\.]*\$'
line = input()
total_income = 0
while line != 'end of shift':
    if re.match(regex, line):
        customer_name, product, quantity, price = re.findall(regex, line)[0]
        price = float(price)
        quantity = int(quantity)
        total_bill = quantity * price
        print(f'{customer_name}: {product} - {total_bill:.2f}')
        total_income += total_bill
    line = input()

print(f'Total income: {total_income:.2f}')
