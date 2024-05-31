
my_tuple = (2, "Python", (3, 5), [2, "Python", (3, 5)], "Maktab",)


my_dict = {}


for i in range(0, len(my_tuple), 2):
    if (i+2) > len(my_tuple):
        break
    key = my_tuple[i]
    value = my_tuple[i + 1]
    my_dict[key] = value

print(my_dict)
