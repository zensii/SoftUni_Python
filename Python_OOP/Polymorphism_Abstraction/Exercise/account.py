class Account:
    def __init__(self, owner: str, amount: int = 0, transactions=None):
        if transactions is None:
            transactions = []
        self.owner = owner
        self.amount = amount
        self._transactions = transactions

    @property
    def balance(self):
        return self.amount + sum(self._transactions)


    def handle_transaction(self, transaction_amount: int):
        self._transactions.append(transaction_amount)
        if self.balance <= 0:
            self._transactions.pop()
            raise ValueError("sorry cannot go in debt!")
        return f"New balance: {self.balance}"

    def add_transaction(self, amount):
        if isinstance(amount, int):
            self.handle_transaction(amount)
        else:
            raise ValueError("please use int for amount")

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, idx):
        return self._transactions[idx]

    def __reversed__(self):
        return self._transactions[::-1]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        return Account(f"{self.owner}&{other.owner}", self.amount + other.amount, self._transactions + other._transactions)


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
