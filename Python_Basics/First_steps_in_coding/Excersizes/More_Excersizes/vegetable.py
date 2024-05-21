N = float(input())
M = float(input())
N_kg = int(input())
M_kg = int(input())

# EUR = 1.94 lev

sum_lev = N * N_kg + M * M_kg

sum_eur = sum_lev / 1.94

print(f"{sum_eur:.2f}")

