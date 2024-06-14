def outer_fun(a:int, b:int):
    def inner_fun(a:int, b: int):
        return a+b +y
    
    s = inner_fun(a, b)
    return s+5

print(outer_fun(5, 10))
