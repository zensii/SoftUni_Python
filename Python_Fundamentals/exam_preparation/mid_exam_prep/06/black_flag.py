pirating_duration = int(input())
plunder_per_day = int(input())
target_plunder = float(input())
accumulated_plunder = 0

for plunder_session in range(1, pirating_duration+1):

    accumulated_plunder += plunder_per_day

    if plunder_session % 3 == 0:
        accumulated_plunder += plunder_per_day * 0.5
    if plunder_session % 5 == 0:
        accumulated_plunder = 0.7 * accumulated_plunder
if accumulated_plunder >= target_plunder:
    print(f'Ahoy! {accumulated_plunder:.2f} plunder gained.')
else:
    print(f'Collected only {accumulated_plunder/target_plunder*100:.2f}% of the plunder.')