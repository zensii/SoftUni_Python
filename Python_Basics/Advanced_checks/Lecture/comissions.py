city = input()
sales = float(input())

commission = 0

if city == 'Sofia':
    if 0 <= sales <= 500:
        commission = 0.05
    elif 500 < sales <= 1000:
        commission = 0.07
    elif 1000 < sales <= 10000:
        commission = 0.08
    elif sales > 10000:
        commission = 0.12
    else:
        print('error')
        exit()

elif city == 'Varna':
    if 0 <= sales <= 500:
        commission = 0.045
    elif 500 < sales <= 1000:
        commission = 0.075
    elif 1000 < sales <= 10000:
        commission = 0.1
    elif sales > 10000:
        commission = 0.13
    else:
        print('error')
        exit()

elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        commission = 0.055
    elif 500 < sales <= 1000:
        commission = 0.08
    elif 1000 < sales <= 10000:
        commission = 0.12
    elif sales > 10000:
        commission = 0.145
    else:
        print('error')
        exit()
else:
    print('error')
    exit()

print(f'{sales * commission:.2f}')
