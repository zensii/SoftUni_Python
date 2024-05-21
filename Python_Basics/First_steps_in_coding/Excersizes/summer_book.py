from math import floor

pages = int(input())
page_per_hour = int(input())
days = int(input())

days_reading = pages/days/page_per_hour

print(floor(days_reading))



