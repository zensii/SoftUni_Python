skumriq_bgn = float(input())
caca_bgn = float(input())

palamud = float(input())
safrid = float(input())
midi = int(input())

palamud_bgn = skumriq_bgn + (skumriq_bgn*0.6)
safrid_bgn = caca_bgn + (caca_bgn*0.8)
midi_bgn = 7.5

total = palamud * palamud_bgn + safrid_bgn * safrid + midi_bgn * midi

print(f"{total:.2f}")



