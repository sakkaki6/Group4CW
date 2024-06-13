list1 = [(1, 2), (2, 5), (4, 4)]
for i in range(len(list1)-1):
    for j in range(i+1, len(list1)):
        if list1[1][len(list1[1])-1] > list1[j][len(list1[j])-1]:
            a = list1[i]
            list1[i] = list1[j]
            list1[j] = a

print(list1)
