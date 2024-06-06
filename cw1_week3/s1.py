min_num = int(input("Enter the minimum : "))
max_num = int(input("Enter the maximum : "))
length = int(input("Enter the number of items in the list: "))

import random

random_list = [random.randint(min_num, max_num) for _ in range(length)]
print(random_list)

