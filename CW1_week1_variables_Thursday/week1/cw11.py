s1 = input("Please enter the first string: ")
s2 = input("Please enter the second string: ")

for char in s1:
    if char not in s2:
        result = "False"
        break
    result = "True"

print(result)
