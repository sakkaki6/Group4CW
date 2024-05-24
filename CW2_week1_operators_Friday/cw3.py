start = int(input())
end = int(input())
for index in range(start, end):
    if index % 2 != 0:
        if index % 3 != 0:
            if index % 5 != 0:
                if index % 7 !=0:
                  print(index)
