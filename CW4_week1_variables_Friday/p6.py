def sed(file_input):
    with open(file_input, 'r') as r:
        k = r.read().split('.')
        d = {}
        counter =0
        for i in range(len(k)):
            for j in k[i]:
                counter+=1
            d[i]= counter
            counter =0
        
        counter =0
        li =[]
        for i in range(len(d)):
            for j in range(i+1, len(d)):
                if d[i] == d[j]:
                    counter +=1
                    if k[i] not in li:
                        li.append(k[i])
                    li.append(k[j])
                    del d[j]
                    
            if counter !=0:
                print(f'{len(li)} sentences have length {counter}')
                print(li)
            else:
                print(f'1 sentence has length {len(k[i])}')
                print(k[i])
            li =[]
            counter =0
                


sed('project7.txt')
