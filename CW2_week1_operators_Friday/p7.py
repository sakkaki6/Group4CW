li1 = ['m', 'na', 'i', 'ke']
li2 = ['y', 'me', 's', 'lly', 'ahmad']
li3 = []
s = ''
if len(li1) <= len(li2):
    for i in range(len(li1)):
        s = li1[i] + li2[i]
        li3.append(s)
else:
    for i in range(len(li2)):
        s = li1[i] + li2[i]
        li3.append(s)
        

if len(li1) < len(li2):
    for j in range(i+1, len(li2)):
        li3.append(li2[j])
elif len(li2) < len(li1):
    for j in range(i+1, len(li1)):
        li3.append(li1[j])

print(li3)

