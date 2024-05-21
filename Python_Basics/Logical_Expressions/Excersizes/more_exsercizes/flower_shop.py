from math import floor, ceil

magnolii = int(input())
ziumbiuli = int(input())
rozes = int(input())
cacti = int(input())
present_price = float(input())

#  prices

magnolii_price = 3.25
ziumbiuli_price = 4
roze_price = 3.5
cactus_price = 8

tax = 0.05

total_gain = (magnolii_price * magnolii + ziumbiuli_price * ziumbiuli
              + roze_price * rozes + cactus_price * cacti) * (1 - tax)

if total_gain >= present_price:
    change = total_gain - present_price
    print(f'She is left with {floor(change)} leva.')
else:
    need_more = present_price - total_gain
    print(f'She will have to borrow {ceil(need_more)} leva.')
