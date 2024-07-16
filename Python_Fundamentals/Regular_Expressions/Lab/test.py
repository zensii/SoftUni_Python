# first code:

import re

string = input("Enter the string: ")
regex = r"\b(\d{2}([.\/-])[A-Z][a-z]{2}\2\d{4})\b"

matches = re.findall(regex, string)
print(matches)
for date in matches:
    day, month, year = re.split(r'[./-]', date[0])
    print(f"Day: {day}, Month: {month}, Year: {year}")


# second code:


string = input()
regex = r"\b(\d{2}([.\/-])[A-Z][a-z]{2}\2\d{4})\b"

dates = [matches[0] for matches in re.findall(regex, string)]
print(dates)
for date in dates:

    day, month, year = re.split('[.-/]', date)
    print(f'Day: {day}, Month: {month}, Year: {year}')
