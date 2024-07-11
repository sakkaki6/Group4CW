class Temperature:
    
    def Celsius_to_Fahrenheit(degree):
        return (degree - 32) * 5/9

    def Fahrenheit_to_Celsius(degree):
        return (1.8*degree)+32

    @classmethod
    def far(cls,degree):
        return cls.Celsius_to_Fahrenheit(0)
    
print (Temperature.far(0))
print(Temperature.Celsius_to_Fahrenheit(0))
print(Temperature.Fahrenheit_to_Celsius(0))
