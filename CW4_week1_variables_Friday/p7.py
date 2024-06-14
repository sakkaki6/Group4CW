def sed(file_input):
    with open(file_input, 'r') as r:
        with open('words2.txt', 'w') as w:
            k = r.read()
            s =''
            for i in k:
                if i =='.' or i=='!' or i=='?':
                    s+=i
                    if s.find('good') != -1:
                        w.write(s)
                    s =''
                    continue
                s+=i


sed('project6.txt')
