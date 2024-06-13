def defualt_val_dict(employees=[], default={}):
    output = dict.fromkeys(employees, default)
    print(output)


defualt_val_dict(['Kelly', 'Emma'], {
                 "designation": 'Developer', "salary": 8000})
