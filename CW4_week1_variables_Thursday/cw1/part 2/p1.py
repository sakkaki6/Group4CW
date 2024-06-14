def sum1(s):
    if s == 0:
        return 0
    return s + sum1(s-1)

s = sum1(10)
print(s)