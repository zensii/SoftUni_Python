ppl_queue = int(input())
lift_state = [int(wagon) for wagon in input().split(' ')]

for wagon in range(len(lift_state)):
    if ppl_queue > 0:
        while lift_state[wagon] < 4:
            if ppl_queue > 0:
                lift_state[wagon] += 1
                ppl_queue -= 1
            else:
                break
    else:
        break

if ppl_queue == 0 and sum(lift_state) < len(lift_state) * 4:
    print('The lift has empty spots!')
elif ppl_queue > 0:
    print(f"There isn't enough space! {ppl_queue} people in a queue!")

print(' '.join(map(str, lift_state)))
