from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    SPONSORS = []
    EXPENSES = 0

    @abstractmethod
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError('F1 is an expensive sport, find more sponsors!')
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        earnings = 0 - self.EXPENSES
        for sponsor in self.SPONSORS:
            for prize in sponsor.values():
                if race_pos <= prize[0][0]:
                    earnings += prize[0][1]
                elif race_pos <= prize[1][0]:
                    earnings += prize[1][1]
        self.budget += earnings
        return f"The revenue after the race is {earnings}$. Current budget {self.budget}$"

