class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print('File opened')
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        
        if isinstance(exc_val, ZeroDivisionError):
            self.file.close()
            print('zero division')
            print('File closed')
            return True
        else:
            self.file.close()
            print('File closed')
        


with FileManager('project1.txt', 'r') as r:
    a = r.read()
    print(a)
    b = 1/0
    