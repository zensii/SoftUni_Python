nums = set(map(int, input().split()))
target = int(input())

while nums:
    first_num = nums.pop()
    second_num = target - first_num
    if second_num in nums:
        print(f"{first_num} + {second_num} = {target}")
        nums.remove(second_num)
