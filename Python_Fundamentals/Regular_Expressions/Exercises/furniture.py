import re
purchases = []
total_price = 0
usr_input = input()
regex = r'^>>([a-zA-Z]+)<<(\d*\.*\d+)!(\d+)$'

while usr_input != 'Purchase':
    purchase = usr_input
    matches = re.findall(regex, purchase)

    if matches:
        purchases.append(matches[0][0])
        total_price += (float(matches[0][1])*int(matches[0][2]))

    usr_input = input()


print('Bought furniture:')

for purchase in purchases:
    print(purchase)
print(f'Total money spend: {total_price:.2f}')
