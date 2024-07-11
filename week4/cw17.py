def factorial(n):
    try:
        if n < 0:
            raise ValueError("Error:input must be positive integer")

        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    except Exception as e:
        print(e)


number = -6
print(f"The factorial of {number} is {factorial(number)}")
