interval_start = input()
interval_end = input()
skipped_letter = input()
counter = 0

for first_letter in range(ord(interval_start), (ord(interval_end)+1)):
    for second_letter in range(ord(interval_start), (ord(interval_end) + 1)):
        for third_letter in range(ord(interval_start), (ord(interval_end) + 1)):
            if (chr(third_letter) != skipped_letter and chr(second_letter) != skipped_letter
                    and chr(first_letter) != skipped_letter):
                counter += 1
                print(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}', end=' ')
print(counter, end=' ')
