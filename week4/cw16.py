def fib(n):
    if n < 0:
        print("Incorrect input")
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


n = 5
fib_number = fib(n)
print(f" {n}th member of fibbo is :{fib_number}")
