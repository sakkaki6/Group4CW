sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89] 

li1 = sample_list[:len(sample_list)//3]
li2 = sample_list[len(sample_list)//3: len(sample_list)//3*2]
li3 = sample_list[len(sample_list)//3*2:]

print(sorted(li1))
print(sorted(li2))
print(sorted(li3))