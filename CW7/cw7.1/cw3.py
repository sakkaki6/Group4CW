class RationalNumber:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator != 0:
             self.denominator = denominator
        self.simplify()

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return RationalNumber(numerator,denominator)
    
    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return RationalNumber(numerator,denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return RationalNumber(numerator,denominator)
    
    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return RationalNumber(numerator,denominator)


    def gcd(numerator,denominator):
        while  denominator:
            numerator,denominator = denominator , numerator%denominator
        return numerator
        

    def simplify(self):
        gcd = RationalNumber.gcd(self.numerator,self.denominator)
        self.numerator//=gcd
        self.denominator //=gcd

    def __str__(self):
        return f'{self.numerator}\{self.denominator}'

a = RationalNumber(16,6)
b = RationalNumber(1,3)

print(a)
print(a+b)
print(a-b)
print(a*b)
print(a/b)