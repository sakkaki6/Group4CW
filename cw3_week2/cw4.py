my_tuple = (2, "Python", (3, 5), [2, "Python", (3, 5)], "Maktab")
list_a = []
for i in range(0, len(my_tuple), 2):
    if (i+2) > len(my_tuple):
        break
    t = (my_tuple[i], my_tuple[i+1])
    list_a.append(t)


print(list_a)
print(dict(list_a))
