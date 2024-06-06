
def count_letter(a):

    upper_case = 0
    lower_case = 0
    
    str2 = a.replace(" ","")
    for i in str2:
        if i.isupper():
            upper_case += 1
        elif i.lower():
            lower_case += 1
        

    print(f"Upper case letters: {upper_case}")
    print(f"Lower case letters: {lower_case}")
    



a = input("enter a string:")
count_letter(a)
