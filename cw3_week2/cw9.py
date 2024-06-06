
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

sample_dict["Location"]=sample_dict.pop('city')
# sample_dict['location'] = sample_dict.pop('city')

print(sample_dict)