
with open ('project1.txt','w')as m:
    m.write("hello")

class FileHandler:
    @classmethod
    def read_file(cls, file_path):
       with open(file_path, 'r') as file:
                return file.read()
        

file_content = FileHandler.read_file('project1.txt')
print(file_content)

    