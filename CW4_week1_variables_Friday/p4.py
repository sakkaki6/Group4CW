def sed(file_input):
    with open(file_input, 'r') as r:
        li =[]
        k = r.read()
        k = k.lower().replace(',',' ')
        k = k.split()
        # print(k)
        for i in k:
            if i==i[::-1] and not i in li:
                li.append(i)
    print(li)
    print('Number of palindromic words:',len(li))

sed('project4.txt')
