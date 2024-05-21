V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

pipe_1_liters = P1 * H
pipe_2_liters = P2 * H

total_liters = pipe_1_liters + pipe_2_liters

pool_filled = total_liters / V * 100

pipe_1 = P1 * H / total_liters * 100
pipe_2 = P2 * H / total_liters * 100

if V >= total_liters:
    print(f"The pool is {pool_filled:.2f}% full. Pipe 1: {pipe_1:.2f}%. Pipe 2: {pipe_2:.2f}%.")
else:
    print(f"For {H} hours the pool overflows with {total_liters - V:.2f} liters.")
