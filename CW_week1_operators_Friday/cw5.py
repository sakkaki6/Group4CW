list1 = [120, 230, 30, 40, 45, 75, 93, 100]
i = 0
while i < len(list1):
    if (list1[i] % 2 == 0 and list1[i] <= 100):
        print('there is a', list1[i], 'at index no:', i)
    i += 1
