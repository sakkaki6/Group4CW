class FileWriter:
    def __init__(self, text) -> None:
        self.text = text

    @classmethod
    def write_to_file(cls, ins):
        with open('text.txt', 'w') as text_file:
            return text_file.write(ins.text)


file1 = FileWriter('hello everybody!')
FileWriter.write_to_file(file1)
