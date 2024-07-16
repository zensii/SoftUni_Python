import re

string = input()
regex = r"\b(\d{2}([.\/-])[A-Z][a-z]{2}\2\d{4})\b"

dates = [matches[0] for matches in re.findall(regex, string)]

for date in dates:

    day, month, year = re.split('[./-]', date)
    print(f'Day: {day}, Month: {month}, Year: {year}')

