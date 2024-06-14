from random import randint

first, end, count = map(int, input().split())
li = []
for i in range(count):
    li.append(randint(first, end))

print(li)
