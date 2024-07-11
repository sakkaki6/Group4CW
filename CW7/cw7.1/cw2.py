class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        self._validate_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        self._validate_currency(other)
        return Money(self.amount - other.amount, self.currency)

    def __eq__(self, other):
        self._validate_currency(other)
        return self.amount == other.amount

    def __lt__(self, other):
        self._validate_currency(other)
        return self.amount < other.amount

    def __gt__(self, other):
        self._validate_currency(other)
        return self.amount > other.amount

    def _validate_currency(self, other):
        if self.currency != other.currency:
            raise ValueError(f"Cannot operate on Money with different currencies: {self.currency} vs {other.currency}")
        
    


    def display(self):
        print(f"{self.amount:.2f} {self.currency}")



money1 = Money(100, 'RIAL')
money2 = Money(50, 'RIAL')
money3 = Money(75, 'EUR')



print("Money 1:")
money1.display()

print("Money 2:")
money2.display()

print("Money 1 + Money 2:")
(money1 + money2).display()

print("Money 1 - Money 2:")
(money1 - money2).display()

print("Money 1 == Money 2:")
print(money1 == money2)

print("Money 1 > Money 2:")
print(money1 > money2)

print("Money 1 < Money 2:")
print(money1 < money2)


