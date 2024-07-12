a = 1
def f():
    a = 2
    b =2
    def g():
        nonlocal b
        global a
        print(a, b)
    g()

f()

class VariableScopeDemo:
    a =1
    def __init__(self) -> None:
        self.b = 2
        VariableScopeDemo.a+=1