from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    BASE_BUDGET = 1000.0

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.BASE_BUDGET)

    def win(self):
        self.advantage += 115
        self.wins += 1

