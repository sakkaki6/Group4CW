# def multiply_list(numbers):
#     result = 1
#     for item in numbers:
#         result *= item
#     return result


#numbers = [8, 2, 3, -1, 7]
# multiply1 = multiply_list(numbers)
# print(multiply1)

import functools

# numbers = [8, 2, 3, -1, 7]
# print("The multiply of the list elements is : ", end="") 
# print(functools.reduce(lambda a, b: a*b,numbers )) 

import operator

numbers = [8, 2, 3, -1, 7]
print("The multiply of the list elements is : ", end="") 
print(functools.reduce(operator.mul,numbers ))

