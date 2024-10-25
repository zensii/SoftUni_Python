from Python_OOP.First_Steps_In_OOP.Exercise.pokemon_battle.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return f"This pokemon is already caught"

    def release_pokemon(self, name:str):
        for available_pokemon in self.pokemons:
            if name == available_pokemon.name:
                self.pokemons.remove(available_pokemon)
                return f"You have released {name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = ''

        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        if self.pokemons:
            for pokemon in self.pokemons:
                result += f"- {pokemon.pokemon_details()}\n"
        return result

