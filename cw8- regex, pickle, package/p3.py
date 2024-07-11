class CustomStack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, grade: str):
        return self.stack.append(grade)
    
    def pop(self):
        return self.stack.pop()
    
    def __len__(self):
        return len(self.stack)
    
    def __repr__(self) -> str:
        s = ''
        for i in self.stack:
            s +=i + ', '
        s = s[:len(s)-2]
        return f'Elements of stack are: {s}'

a = CustomStack()
a.push('10')
a.push('11')
print('pop is:', a.pop())
a.push('12')
a.push('13')
a.push('14')
a.pop()
print('len a is:', len(a))
print(repr(a))