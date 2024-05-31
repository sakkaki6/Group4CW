list1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
a = len(list1)

b = a//3
chunk1 = list1[:b]
chunk2 = list1[b:2*b]
chunk3 = list1[2*b:]

chunk1.reverse()
chunk2.reverse()
chunk3.reverse()


print(chunk1, chunk2, chunk3)
