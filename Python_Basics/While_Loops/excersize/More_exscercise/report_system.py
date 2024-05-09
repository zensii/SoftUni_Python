amount_needed = int(input())
card_payment = 0
current_amount = 0
total_cash_payment = 0
num_cash_payments = 0
total_card_payments = 0
num_card_payments = 0

while True:
    entry = input()
    if entry != 'End':
        price = int(entry)

        if card_payment % 2 == 0:
            if price <= 100:
                current_amount += price
                print('Product sold!')
                total_cash_payment += price
                num_cash_payments += 1

            else:
                print('Error in transaction!')
        else:
            if price >= 10:
                current_amount += price
                print('Product sold!')
                total_card_payments += price
                num_card_payments += 1
            else:
                print('Error in transaction!')
        card_payment += 1

    else:
        print('Failed to collect required money for charity.')
        break

    if current_amount >= amount_needed:
        print(f'Average CS: {total_cash_payment / num_cash_payments:.2f}')
        print(f'Average CC: {total_card_payments / num_card_payments:.2f}')
        break
