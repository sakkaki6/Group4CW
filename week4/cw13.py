
def fib(n): 
    a=0
    b=1
    for i in range(n):
        b,a = a+b, b 
        yield a 


print(list(fib(10)))
