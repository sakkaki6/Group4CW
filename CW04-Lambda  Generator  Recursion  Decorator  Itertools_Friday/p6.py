def fibonacci_generator(n):
    a =0
    b =1
    for i in range(n):
        b , a = a+b, b
        yield a 


fib_gen = fibonacci_generator(10) 
for _ in fib_gen: 
    print(_, end=' ') 