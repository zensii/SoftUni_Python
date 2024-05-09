last_sector = input()
first_sector_rows = int(input())
odd_row_seats = int(input())
sector_counter = 0
total_seats = 0

for sector in range(ord('A'), ord(last_sector)+1):

    sector_counter += 1

    for row in range(1, first_sector_rows+sector_counter):

        if row % 2 != 0:

            for seat in range(ord('a'), ord('a')+odd_row_seats):
                print(f'{chr(sector)}{row}{chr(seat)}')
                total_seats += 1
        else:

            for seat in range(ord('a'), ord('a') + odd_row_seats + 2):

                print(f'{chr(sector)}{row}{chr(seat)}')
                total_seats += 1
print(total_seats)
