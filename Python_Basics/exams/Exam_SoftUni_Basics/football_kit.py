tshirt_price = float(input())
target_sum = float(input())

shorts_price = tshirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = (tshirt_price + shorts_price) * 2

total_spent = (tshirt_price + shorts_price + socks_price + shoes_price) * 0.85

if total_spent >= target_sum:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_spent:.2f} lv.')
else:
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {target_sum - total_spent:.2f} lv. more.')
