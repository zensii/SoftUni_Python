class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            return f"Mammals in {zoo_name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == 'fish':
            return f"Fishes in {zoo_name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        if species == 'bird':
            return f"Birds in {zoo_name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
n = int(input())
zoo = Zoo(zoo_name)

for i in range(n):
    animal = input().split()
    species, name = animal
    zoo.add_animal(species, name)

request_info = input()
print(zoo.get_info(request_info))
