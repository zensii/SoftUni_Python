from typing import List


from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    VALID_EQUIPMENT = {"KneePad":KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPE = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value


    def add_equipment(self, equipment_type: str):

        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception("Invalid equipment type!")
        new_equipment = self.VALID_EQUIPMENT[equipment_type]
        self.equipment.append(new_equipment())
        return f"{equipment_type} was successfully added."


    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):

        if team_type not in self.VALID_TEAM_TYPE:
            raise Exception("Invalid team type!")
        if len(self.teams) >= self.capacity:
            return f"Not enough tournament capacity."
        new_team = self.VALID_TEAM_TYPE[team_type]
        self.teams.append(new_team(team_name, country, advantage))
        return f"{team_type} was successfully added."


    def sell_equipment(self, equipment_type: str, team_name: str):
        eq_to_sell = self.get_equipment_by_type(equipment_type)
        team_to_buy = self.get_team_by_name(team_name)

        if team_to_buy.budget >= eq_to_sell.price:
            team_to_buy.budget -= eq_to_sell.price
            team_to_buy.equipment.append(eq_to_sell)
            self.equipment.remove(eq_to_sell)
            return f"Successfully sold {equipment_type} to {team_name}."

        raise Exception(f"Budget is not enough!")


    def remove_team(self, team_name: str):

        try:
            team_to_remove = self.get_team_by_name(team_name)
        except IndexError:
            raise Exception("No such team!")

        if team_to_remove.wins:
            raise Exception(f"The team has {team_to_remove.wins} wins! Removal is impossible!")

        self.teams.remove(team_to_remove)
        return f"Successfully removed {team_name}."


    def increase_equipment_price(self, equipment_type: str):

        equipment_increased = [e.increase_price() for e in self.equipment if type(e).__name__ == equipment_type]
        return f"Successfully changed {len(equipment_increased)}pcs of equipment."


    def play(self, team_name1: str, team_name2: str):

        team_one = self.get_team_by_name(team_name1)
        team_two = self.get_team_by_name(team_name2)

        if not type(team_one).__name__ == type(team_two).__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        winner = None
        team_one_strength = team_one.advantage + sum([e.protection for e in team_one.equipment])
        team_two_strength = team_two.advantage + sum([e.protection for e in team_two.equipment])
        if team_one_strength > team_two_strength:
            winner = team_one
            team_one.win()
        elif team_two_strength > team_one_strength:
            winner = team_two
            team_two.win()
        if winner:
            return f"The winner is {winner.name}."
        return "No winner in this game."


    def get_statistics(self):
        result = (f"Tournament: {self.name}\n"
                  f"Number of Teams: {len(self.teams)}\n"
                  f"Teams:")
        for team in sorted(self.teams, key=lambda t: -t.wins):
            result += f"\n{team.get_statistics()}"

        return result


    def get_equipment_by_type(self, equipment_type):
        return [e for e in self.equipment if e.__class__.__name__ == equipment_type][-1]


    def get_team_by_name(self, team_name):
        return [team for team in self.teams if team.name == team_name][0]


