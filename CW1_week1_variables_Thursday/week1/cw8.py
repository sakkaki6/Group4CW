def compare(list1):
    if list1[0]!=list1[len(list1)-1]:
        result = False
    else: 
        result = True
    return print(result)

inp1 =input('enter a list:')

compare(inp1)