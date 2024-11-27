from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    BASE_RATE = 1.5
    BASE_AMOUNT = 2000.0
    LOAN_TYPE = 'StudentLoan'
    def __init__(self):
        super().__init__(self.BASE_RATE, self.BASE_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.2