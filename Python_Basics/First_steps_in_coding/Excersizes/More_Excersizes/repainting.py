X = float(input())
Y = float(input())
h = float(input())

green_area = ((X*X*2)-(2*1.2)) + ((Y*X*2)-(1.5*1.5*2))
red_area = (X*Y*2) + (X*h)

red_paint = red_area / 4.3
green_paint = green_area / 3.4

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")

