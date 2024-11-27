from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    BASE_RATE = 3.5
    BASE_AMOUNT = 50000.0
    LOAN_TYPE = 'MortgageLoan'
    def __init__(self):
        super().__init__(self.BASE_RATE, self.BASE_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5