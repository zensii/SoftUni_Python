add = 30

max = 100

current = 80

max gain = 100 - current

if max_gain >= add

    current += add

else:
    current += current + add - max

if 100 - current_energy >= energy_gain:
    current_energy += energy_gain
else:
    current_energy += current_energy + energy_gain - 100