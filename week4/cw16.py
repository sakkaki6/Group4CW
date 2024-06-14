def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


n = 10
fib_number = fib(n-2)
print(f" {n}th member of fibbo is :{fib_number}")
