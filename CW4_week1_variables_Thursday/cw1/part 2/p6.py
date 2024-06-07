def pascal(n:int):
    li1 = [1]
    li2 = [1, 1]
    print(li1)
    print(li2)
    for i in range(2, n):
        if i%2 == 0:
            li1.append(0)
            for j in range(1,i):
                li1[j] = (li2[j-1]+ li2[j])
            li1.append(1)
            print(li1)
        else:
            li2.append(0)
            for j in range(1,i):
                li2[j] = (li1[j-1]+ li1[j])
            li2.append(1)
            print(li2)

pascal(10)