voucher_amount = int(input())

movie_tickets = 0
other_goods = 0
end = False

while True:
    command = input()
    if command == 'End':
        break
    else:

        price = 0
        if len(command) > 8:
            movie_title = command
            for char in movie_title[0:2]:
                price += ord(char)
            if price > voucher_amount:
                end = True
                break
            movie_tickets += 1
        else:
            purchase = command
            for char in purchase[0:1]:
                price += ord(char)
                if price > voucher_amount:
                    end = True
                    break
                other_goods += 1

        voucher_amount -= price

    if end:
        break
print(movie_tickets)
print(other_goods)

