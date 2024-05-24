input1 = input('please enter a combined string:')

letters = 0
digits = 0
special_symbols = 0

for char in input1:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif not char.isspace():
        special_symbols += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special Symbols:", special_symbols)
