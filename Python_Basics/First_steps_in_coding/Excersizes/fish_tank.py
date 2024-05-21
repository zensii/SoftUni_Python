L = int(input())
W = int(input())
H = int(input())
fill = float(input())

volume = L*W*H
liter = volume/1000

water = liter - liter * fill/100

print(water)


