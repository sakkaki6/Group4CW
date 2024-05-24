start = int(input())
end = int(input())
c = 1
for index in range(start, end+1):
    if index%2==0:
        continue
    for index2 in range(3,index//2,2):
        if index%index2==0:
            c = 0
            break
    
    if c==0:
        c-1
        print(index)

