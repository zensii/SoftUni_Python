from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan

class BankApp:

    LOAN_TYPES = {"StudentLoan":StudentLoan, "MortgageLoan": MortgageLoan}
    CLIENT_TYPES = {"Student":Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")

        new_loan = self.LOAN_TYPES[loan_type]
        self.loans.append(new_loan())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return f"Not enough bank capacity."

        new_client = self.CLIENT_TYPES[client_type]
        self.clients.append(new_client(client_name, client_id, income))
        return f"{client_type} was successfully added."


    def grant_loan(self, loan_type: str, client_id: str):

        client = [c for c in self.clients if c.client_id == client_id][0]
        loan = [l for l in self.loans if l.__class__.__name__ == loan_type][0]

        if type(client).__name__[0] == loan_type[0] or (type(client).__name__[0] == 'A' and loan_type[0] == 'M'):
            client.loans.append(loan)
            self.loans.remove(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        try:
            client = [c for c in self.clients if c.client_id == client_id][0]
        except IndexError:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."


    def increase_loan_interest(self, loan_type: str):
        counter = 0
        for loan in self.loans:
            if type(loan).__name__ == loan_type:
                loan.increase_interest_rate()
                counter += 1
        return f"Successfully changed {counter} loans."


    def increase_clients_interest(self, min_rate: float):
        to_increase = [c.increase_clients_interest() for c in self.clients if c.interest < min_rate]
        return f"Number of clients affected: {len(to_increase)}."


    def get_statistics(self):
        result = [f"Active Clients: {len(self.clients)}", f"Total Income: {sum([c.income for c in self.clients]):.2f}",
                  f"Granted Loans: {sum(len(c.loans) for c in self.clients)}, Total Sum: {sum([c.total_loan() for c in self.clients]):.2f}",
                  f"Available Loans: {len(self.loans)}, Total Sum: {sum([l.amount for l in self.loans]):.2f}",
                  f"Average Client Interest Rate: {sum([c.interest for c in self.clients]) / len(self.clients) if len(self.clients) != 0 else 0:.2f}"]
        return '\n'.join(result)


