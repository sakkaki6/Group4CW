
li =[]
def sed(file_input):
    with open(file_input, 'r') as r:
        k = r.read().split()
        for i in k:
            li.append(i)
    return li

sed('file1-3.txt')
sed('file2-3.txt')
sed('file3-3.txt') 

def wr(li):
    counter =0
    li_final =[]
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i]==li[j] and li[i] not in li_final:
                li_final.append(li[i])
                counter+=1
    print(li_final)
    print(counter)


wr(li)
    

