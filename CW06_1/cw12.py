class StringUtil:
    @classmethod
    def reverse_string(cls, input_string):
        return input_string[::-1]


reversed_string = StringUtil.reverse_string("hello")
print(reversed_string)
