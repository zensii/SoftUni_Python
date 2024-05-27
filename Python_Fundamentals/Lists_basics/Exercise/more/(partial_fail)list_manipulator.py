string_nums = [int(nums) for nums in input().split()]
command = input().split()

while command[0] != 'end':

        if command[0] == 'exchange':
            index = int(command[1])
            if 0 <= index < len(string_nums):
                string_nums = string_nums[index+1:] + string_nums[:index+1]

            else:
                print('Invalid index')

        elif command[0] == 'max':
            max_index = None
            max_value = None

            if command[1] == 'even':
                for i in range(len(string_nums) - 1, -1, -1):
                    if string_nums[i] % 2 == 0 and (max_value is None or string_nums[i] > max_value):
                        max_index = i
                        max_value = string_nums[i]

            elif command[1] == 'odd':
                for i in range(len(string_nums) - 1, -1, -1):
                    if string_nums[i] % 2 != 0 and (max_value is None or string_nums[i] > max_value):
                        max_index = i
                        max_value = string_nums[i]

            if max_index is not None:
                print(max_index)
            else:
                print('No matches')

        elif command[0] == 'min':
            min_index = None
            min_value = None
            if command[1] == 'even':
                for i in range(len(string_nums) - 1, -1, -1):
                    if string_nums[i] % 2 == 0 and (min_value is None or string_nums[i] < min_value):
                        min_index = i
                        min_value = string_nums[i]

            elif command[1] == 'odd':
                for i in range(len(string_nums) - 1, -1, -1):
                    if string_nums[i] % 2 != 0 and (min_value is None or string_nums[i] < min_value):
                        min_index = i
                        min_value = string_nums[i]
            if min_index is not None:
                print(min_index)
            else:
                print('No matches')

        if command[0] == 'first':
            count = int(command[1])
            if count > len(string_nums):
                print('Invalid count')
            else:
                if command[2] == 'even':
                    first_count = []
                    counter = int(command[1])

                    for i in range(len(string_nums)):
                        if string_nums[i] % 2 == 0:
                            first_count.append(string_nums[i])

                            if len(first_count) == counter:
                                break
                else:
                    first_count = []
                    counter = int(command[1])

                    for i in range(len(string_nums)):
                        if string_nums[i] % 2 != 0:
                            first_count.append(string_nums[i])

                            if len(first_count) == counter:
                                break
                print(first_count)

        elif command[0] == 'last':
            count = int(command[1])
            if count > len(string_nums):
                print('Invalid count')
            else:
                if command[2] == 'even':
                    last_count = []
                    counter = int(command[1])

                    for i in range(len(string_nums) - 1, -1, -1):
                        if string_nums[i] % 2 == 0:
                            last_count.append(string_nums[i])

                            if len(last_count) == counter:
                                break
                else:
                    last_count = []
                    counter = int(command[1])

                    for i in range(len(string_nums) - 1, -1, -1):
                        if string_nums[i] % 2!= 0:
                            last_count.append(string_nums[i])

                            if len(last_count) == counter:
                                break
                print(last_count[::-1])   # <<<< crucial miss on my part as when we start from end of the list the resulting list is also reversed which is undesirable
        command = input().split()

print(string_nums)
