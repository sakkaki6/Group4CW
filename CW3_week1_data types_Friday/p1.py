li = [(2,5), (1,2), (4,4), (3, 4, 3)]

for i in range(len(li)-1):
    for j in range(i+1, len(li)):
        if li[i][len(li[i])-1] > li[j][len(li[j])-1]:
            a = li[i]
            li[i]=li[j]
            li[j]=a


print(li)