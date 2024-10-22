class Player:

    def __init__(self, name:str, hp: int, mp: int):
        self.mp = mp
        self.hp = hp
        self.name = name
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return f"Skill already added"

    def player_info(self):

        return (f"Name: {self.name}\n" +
                f"Guild: {self.guild}\n" +
                 f"HP: {self.hp}\n" +
                   f"MP: {self.mp}\n" +
                     '\n'.join([f"==={skill_name} - {skill_cost}" for skill_name, skill_cost in self.skills.items()]))

#
# if __name__ == "__main__":
#     player = Player("George", 50, 100)
#     print(player.add_skill("Shield Break", 20))
#     print(player.player_info())
