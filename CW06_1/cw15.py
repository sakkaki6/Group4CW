import json

class Converter:
    @classmethod
    def json_to_dict(cls, json_string):
       return json.loads(json_string)
        

json_string = '{"name": "ali", "age": 30, "city": "tehran"}'
python_dict = Converter.json_to_dict(json_string)
print(python_dict)  
