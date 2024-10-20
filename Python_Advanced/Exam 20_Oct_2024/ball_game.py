from collections import deque

str_need = list(map(int, input().split(' ')))
acc_need = deque(map(int, input().split(' ')))
goals = 0

while str_need and acc_need:
    curr_str = str_need.pop()
    curr_acc = acc_need.popleft()

    if curr_str + curr_acc == 100:
        goals += 1
    elif curr_str + curr_acc > 100:
        curr_str -= 10
        str_need.append(curr_str)
        acc_need.append(curr_acc)
    else:
        if curr_str < curr_acc:
            acc_need.appendleft(curr_acc)
        elif curr_str > curr_acc:
            str_need.append(curr_str)
        else:
            str_need.append(curr_str + curr_acc)

if goals == 3:
    print("Paul scored a hat-trick!")
elif goals == 0:
    print("Paul failed to score a single goal.")
elif goals > 3:
    print("Paul performed remarkably well!")
elif 0 < goals < 3:
    print("Paul failed to make a hat-trick.")

if goals:
    print(f"Goals scored: {goals}")

if str_need:
    print(f"Strength values left: {', '.join(map(str, str_need))}")
if acc_need:
    print(f"Accuracy values left: {', '.join(map(str, acc_need))}")