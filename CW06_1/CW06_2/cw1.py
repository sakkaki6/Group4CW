class Vehicle:
    def __init__(self, make, model, year:int):
        self._make = make
        self._model = model
        self._year = year

    
    def display_detail(self):
        return f"make: {self.make}, model: {self.model}, year: {self.year}"

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        if make=='':
            raise ValueError("Make must be a non-empty string.")
        self._make = make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if model=='':
            raise ValueError("Model must be a non-empty string.")
        self._model = model

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if year <= 0:
            raise ValueError("Year must be a positive integer.")
        self._year = year



car = Vehicle("Toyota", "Camry", 2021)
print(car.display_detail())

    
car.make = "Honda"
car.model = "Accord"
car.year = 2022
print(car.display_detail())

 