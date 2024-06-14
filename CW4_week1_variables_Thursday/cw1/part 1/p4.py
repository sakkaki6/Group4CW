def palindrome(s:str):
    s_reverse = ''
    for i in range(len(s)-1, -1, -1):
        s_reverse += s[i]
    if s == s_reverse:
        print('True')
    else:
        print(False) 

s = input()
palindrome(s)
