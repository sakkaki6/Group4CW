class City:
    def __init__(self, name, population, area) -> None:
        self._name = name
        self._population = population
        self._area = area

    def display_details(self):
        return f"the city name is :{self._name} with {self._population} population and {self._area} square km)"

    @property
    def name(self):
        self._name

    @name.setter
    def name(self, name):
        if name == '':
            raise ValueError("brand must be a non-empty string.")
        self._name = name

    @property
    def population(self):
        self._population

    @population.setter
    def population(self, population):
        if population <= 0:
            raise ValueError("Year must be a positive integer.")
        self._population = population

    @property
    def area(self):
        self._area

    @area.setter
    def area(self, area):
        if area <= 0:
            raise ValueError("area must be a positive integer.")
        self._area = area


city1 = City('tabriz', 120000, 4300)
print(city1.display_details())
city1.name = 'orumie'
city1.population = 10000
city1.area = 800
print(city1.display_details())
