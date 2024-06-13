
num1 = int(input())
Sum = 0
for i in range(1, num1):
    if (num1 % i == 0):
        Sum += i
if (Sum == num1):
    print("true")
else:
    print("false")
