def is_power(a: int, b: int):
    s = b
    while True:
        if a == s:
            return True
        elif a > s:
            s = s*b
        else:
            return False


print(is_power(127, 2))
print(is_power(27, 3))
