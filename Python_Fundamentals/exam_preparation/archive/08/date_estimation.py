import datetime
ref_date = datetime.date(2018, 8, 26)
check_date = input()
year, month, day = map(int, check_date.split('-'))
date = datetime.date(year, month, day)

if date < ref_date:
    print('Passed')
elif date == ref_date:
    print('Today date')
else:
    d = date-ref_date
    print(f"{d.days+1} days left")
