def f(d:dict):
    li =[]
    for i in d.values():
        li.append(i)
    
    d1 ={}
    li = sorted(li, reverse=True)
    for i in li[:3]:
        for k, j in d.items():
            if i == j:
                d1.update({k:j})
    print(d1) 




f({'T-shirt': 45.50, 'Pants': 35, 'Sneakers': 41.30, 'Hat': 55, 'Backpack': 24} )
