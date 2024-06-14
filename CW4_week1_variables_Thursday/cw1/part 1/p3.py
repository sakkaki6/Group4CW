def counting_letters(s:str):
    upper =0
    lower =0
    for i in s:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print('No. of lower case characters:', lower)
    print('No. of upper case characters:', upper)


n = input()
counting_letters(n)