class MathUtil:
    @classmethod
    def is_prime(cls, num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True


print(MathUtil.is_prime(2))
print(MathUtil.is_prime(4))
print(MathUtil.is_prime(17))
print(MathUtil.is_prime(18))
