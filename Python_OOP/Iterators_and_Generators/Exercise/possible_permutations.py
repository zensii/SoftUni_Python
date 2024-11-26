from itertools import permutations

def possible_permutations(my_list):
    all_perm = permutations(my_list)
    for perm in all_perm:
        yield list(perm)

[print(n) for n in possible_permutations([1, 2, 3])]