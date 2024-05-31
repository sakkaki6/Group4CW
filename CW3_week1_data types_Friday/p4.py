def f(t):
    di ={}
    for i in range(0,len(t)-1,2):
        di.update( {t[i]: t[i+1]})
    
    print(di)

f((2, "Python", (3, 5), [2, "Python", (3, 5)], "Maktab") )