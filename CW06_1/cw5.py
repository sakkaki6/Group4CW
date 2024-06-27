class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age =age

class Student(Person):
    def __init__(self, name, age,student_id):
        super().__init__(name,age)
        self.student_id = student_id

person = Person("Ali", 30)
print(f"Name: {person.name}, Age: {person.age}")

student = Student("Behnam", 20, "S12345")
print(f"Name: {student.name}, Age: {student.age}, Student ID: {student.student_id}") 

