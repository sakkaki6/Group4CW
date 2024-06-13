def sum_of_num(a):
    if a == 0:
        return 0
    else:
        return a + sum_of_num(a - 1)
    

res = sum_of_num(10)
print(f"The sum of numbers from 0 to 10 is:{res}")
