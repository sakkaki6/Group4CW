class MathUtils:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multyply(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def power(self):
        return self.a ** self.b

    def floor_division(self):
        return self.a // self.b

    def reminder(self):
        return self.a % self.b