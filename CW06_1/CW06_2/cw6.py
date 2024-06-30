class Student:
    def __init__(self, first_name, last_name, grade:float) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._grade = grade

    def display_details(self):
        return f"the student name is :{self._first_name} {self._last_name}  and {self._grade}% grade)"

    @property
    def first_name(self):
        self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name == '':
            raise ValueError("name must be a non-empty string.")
        self._first_name = first_name

    @property
    def last_name(self):
        self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name == '':
            raise ValueError("last name must be a non-empty string.")
        self._last_name = last_name

    @property
    def grade(self):
        self._grade

    @grade.setter
    def grade(self, grade):
        if grade <= 0 or grade > 100:
            raise ValueError(
                "grade must be a positive integer bethween 0 and 5.")
        self._grade = grade


student1 = Student('ali', 'alavi', 80)
print(student1.display_details())
student1.first_name = 'hasan'
student1.last_name = 'ahmadi'
student1.grade = 98
print(student1.display_details())
