def pangram(s:str):
    se = set()
    for i in s.lower():
        if i.isalpha():
            se.add(i)
    
    if len(se) != 26:
        return False
    else:
        return True
    
print(pangram('the quick brown fox jumps over the laZy doG'))
