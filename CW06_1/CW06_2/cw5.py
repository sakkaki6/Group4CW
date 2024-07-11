class Resturante:
    def __init__(self, name, cuisine_type, rating:float) -> None:
        self._name = name
        self._cuisine_type = cuisine_type
        self._rating = rating

    def display_details(self):
        return f"the resturant name is :{self._name} with {self._cuisine_type} type and {self._rating} rating)"

    @property
    def name(self):
        self._name

    @name.setter
    def name(self, name):
        if name == '':
            raise ValueError("name must be a non-empty string.")
        self._name = name

    @property
    def cuisine_type(self):
        self._cuisine

    @cuisine_type.setter
    def cuisine_type(self, cuisine_type):
        if cuisine_type == '':
            raise ValueError("cuisine type must be a non-empty string.")
        self._cuisine_type = cuisine_type

    @property
    def rating(self):
        self._rating

    @rating.setter
    def rating(self, rating):
        if rating <= 0 or rating > 5:
            raise ValueError(
                "rating must be a positive integer bethween 0 and 5.")
        self._rating = rating


resturante1 = Resturante('borke', '[kabab,geymeh,pizza]', 4)
print(resturante1.display_details())
resturante1.name = 'atish'
resturante1.cuisine_type = '[gormeh,fesenjan]'
resturante1.rating = 3.4
print(resturante1.display_details())
