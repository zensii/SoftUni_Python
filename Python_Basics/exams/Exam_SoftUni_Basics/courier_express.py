weight = float(input())
type_service = input()
distance = int(input())
price = 0

if type_service == 'standard':
    if weight < 1:
        price = 0.03
    elif 1 <= weight < 10:
        price = 0.05
    elif 10 <= weight < 40:
        price = 0.10
    elif 40 <= weight < 90:
        price = 0.15
    elif 90 <= weight < 150:
        price = 0.20
elif type_service == 'express':
    if weight < 1:
        price = 0.03 + 0.03 * 0.8 * weight
    elif 1 <= weight < 10:
        price = 0.05 + 0.05 * 0.4 * weight
    elif 10 <= weight < 40:
        price = 0.10 + 0.10 * 0.05 * weight
    elif 40 <= weight < 90:
        price = 0.15 + 0.15 * 0.02 * weight
    elif 90 <= weight < 150:
        price = 0.20 + 0.20 * 0.01 * weight

total_cost = price * distance
print(f'The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_cost:.2f} lv.')
