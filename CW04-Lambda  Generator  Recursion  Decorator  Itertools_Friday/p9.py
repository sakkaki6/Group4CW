def fibonacci(n):
    if n==0 or n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = 5 
fib_number = fibonacci(n) 
print(f"The {n}th number of the Fibonacci sequence is: {fib_number}")