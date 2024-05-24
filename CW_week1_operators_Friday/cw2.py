list1 = [12, 43, 55, 25, 230, 400, 145, 501, 50]
list1.sort()
for index in list1:
    if index > 500:
        break
    if (index % 5) == 0:
        if index > 150:
            break
        print(index)
