def remove_pokemon(chain, index):

    removed_pokemon_value = chain[index]

    for i in range(len(chain)):

        if chain[i] <= removed_pokemon_value:
            chain[i] += removed_pokemon_value
        else:
            chain[i] -= removed_pokemon_value

    chain.pop(index)

    return chain, removed_pokemon_value


def swap_pokemon(chain, index):

    removed_pokemon_value = 0
    if index < 0:
        index = 0
        chain, removed_pokemon_value = remove_pokemon(chain, index)
        chain.insert(0, chain[-1])

    elif index >= len(chain):
        index = len(chain) - 1
        chain, removed_pokemon_value = remove_pokemon(chain, index)
        chain.append(chain[0])

    return chain, removed_pokemon_value


pokemon_chain = list(map(int, input().split()))
total_removed_pokemon_value = 0

while len(pokemon_chain) > 0:

    target_index = int(input())

    if 0 <= target_index < len(pokemon_chain):
        pokemon_chain, removed_value = remove_pokemon(pokemon_chain, target_index)
    else:
        pokemon_chain, removed_value = swap_pokemon(pokemon_chain, target_index)

    total_removed_pokemon_value += removed_value

print(total_removed_pokemon_value)
