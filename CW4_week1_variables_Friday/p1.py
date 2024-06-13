with open('s03\project1.txt', 'r') as f:
    li =[]
    s =''
    final_li =[]
    counter_length =0
    final_counter_length = 0
    counter_word =0
    final_counter_word = 0
    for i in f:
        for j in i:
            if j =='.':
                counter_word+=1
                li.append(s)
                s =''
                if counter_word > final_counter_word:
                    final_counter_word = counter_word
                    final_counter_length = counter_length
                    final_li= li[:]
                    counter_length =0    
                    counter_word =0
                    li.clear()
                else:
                    counter_length =0    
                    counter_word =0
                    li.clear()
                    
            elif ord(j) == 32 and counter_length != 0:
                counter_length+=1
                counter_word+=1
                li.append(s)
                s =''
            else:
                counter_length+=1
                s +=j
                

       
    print(final_counter_word)
    print(final_counter_length)
    print(*final_li)






