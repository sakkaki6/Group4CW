strings_list = ["apple", "banana", "Orange", "grape", "kiwi"]

li = list(map(lambda x: x.upper(), strings_list))

li_filter = list(filter(lambda x: False if x.count('A') else True, li))
print(li_filter)