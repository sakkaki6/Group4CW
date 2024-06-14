def ispower(a:int, b:int):
    s =b
    while True:
        if a == s:
            return True
        elif a>s:
            s = s*b
        else:
            return False

print(ispower(127, 2))
print(ispower(27, 3))