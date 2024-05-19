import math

passengers = int(input())
capacity = int(input())

trips = math.ceil(passengers / capacity)
print(trips)
