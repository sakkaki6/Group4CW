import os

class TemporaryFile:
    def __init__(self, filename):
        self.filename = filename

        with open(self.filename, 'w') as f:
            f.write('Temporary file content')
        print(f"\nTemporary file '{self.filename}' created.")

    def __del__(self):
        os.remove(self.filename)
        print(f"\nTemporary file '{self.filename}' deleted.")
        
def test_temporary_file():
    temp_file = TemporaryFile('file1.txt')
   
    
    del temp_file

test_temporary_file()
