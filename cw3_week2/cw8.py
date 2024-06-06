sample_dic ={
"name": "Kelly",
"age": 25,
"salary": 8000,
 "city": "New york"}

keys = ["name", "salary"]


new_dict = {key: sample_dic[key] for key in keys}

print(new_dict)