
num1 = input()
num2 = num1.split(' ')
y = int(num2[0])
x = int(num2[1])
if x <= 10:
    print("Right", (11 - y), x)
else:
    print("Left", (11 - y), (21 - x))
