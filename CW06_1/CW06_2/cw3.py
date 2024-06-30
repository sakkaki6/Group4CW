class Laptop:
    def __init__(self, brand, ram, storage) -> None:
        self._brand = brand
        self._ram = ram
        self._storage = storage

    def display_details(self):
        return f"brand :{self._brand}, ram :{self._ram} GB,storage :{self._storage} GB"

    @property
    def brand(self):
        self._brand

    @brand.setter
    def brand(self, brand):
        if brand == '':
            raise ValueError("brand must be a non-empty string.")
        self._brand = brand

    @property
    def ram(self):
        self._ram

    @ram.setter
    def ram(self, ram):
        if ram <= 0:
            raise ValueError("Year must be a positive integer.")
        self._ram = ram

    @property
    def storage(self):
        self._storage

    @storage.setter
    def storage(self, storage):
        if storage <= 0:
            raise ValueError("Year must be a positive integer.")
        self._storage = storage


laptop1 = Laptop('asus', 4, 64)
print(laptop1.display_details())

laptop1.brand = ('lenovo')
laptop1.ram = 6
laptop1.storage = 128
print(laptop1.display_details())
