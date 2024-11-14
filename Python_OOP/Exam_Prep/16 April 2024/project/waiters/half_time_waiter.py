from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):

    WAGE = 12

    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)

    def calculate_earnings(self):
        return self._hours_worked * self.WAGE

    def report_shift(self):
        return f"{self.name} worked a half-time shift of {self.hours_worked} hours."