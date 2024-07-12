class FileReaderIterator:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __iter__(self):
        return self

    def __next__(self):
        try:
            for i in self.file.readline():
                return i
        except:
            raise StopIteration
    
    def __enter__(self):
        print('File opened')
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('File closed')
        self.file.close()

with FileReaderIterator('project1.txt', 'r') as r:
    print(next(r))
    print(next(r))
    