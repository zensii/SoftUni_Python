def check_possible_distribution(population, minimum):
    total_wealth = sum(population_wealth)
    if total_wealth < len(population) * minimum_wealth:
        print('No equal distribution possible')
        return False
    else:
        return True


def distribute(population_wealth, minimum_wealth):

    while minimum_wealth > min(population_wealth):

        for i in range(len(population_wealth)):
            index_to_reduce = population_wealth.index(max(population_wealth))

            if population_wealth[i] < minimum_wealth:
                amount_to_reduce = minimum_wealth - min(population_wealth)
                population_wealth[index_to_reduce] -= amount_to_reduce
                population_wealth[i] += amount_to_reduce

    return population_wealth


population_wealth = list(map(int, input().split(', ')))
minimum_wealth = int(input())

if check_possible_distribution(population_wealth, minimum_wealth):
    print(distribute(population_wealth, minimum_wealth))




