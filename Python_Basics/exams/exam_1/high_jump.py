target_height = int(input())
total_jumps = 0
end = False
jump_height = 0

for height in range(target_height-30, target_height + 5, 5):
    for trial in range(1, 4):
        jump_height = int(input())
        total_jumps += 1
        if jump_height > height:
            if height >= target_height:
                print(f'Tihomir succeeded, he jumped over {target_height}cm after {total_jumps} jumps.')
                end = True
                break
            height += 5
            break
        if jump_height <= height and trial == 3:
            print(f'Tihomir failed at {height}cm after {total_jumps} jumps.')
            end = True
            break
    if end:
        break
