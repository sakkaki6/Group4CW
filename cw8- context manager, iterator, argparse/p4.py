import time

class Timer:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print('File opened')
        self.start_time = time.time()
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print(time.time() - self.start_time)
        print('File closed')
          

with Timer('project1.txt', 'r') as r:
    a = r.read()
    time.sleep(3)