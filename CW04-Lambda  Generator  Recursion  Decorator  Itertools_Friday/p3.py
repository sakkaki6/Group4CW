tuples_list = [('Hello', 'World'), ('Open', 'AI'), ('GPT', '3')]

li = list(map(lambda x: str(x[0])+' '+str(x[1]), tuples_list))
print(li)