from shape import Shape

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.__radius = radius # private attribute
        self._type = 'Circle'  # protected attribute inherite from Shape
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        self.__radius = value

    # override the abstract method area from Shape
    def area(self):
        return 3.14 * self.__radius ** 2
    
    # override the __str__ method from Shape
    def __str__(self) -> str:
        # super class return type and name, now add radius to the returned string
        return super().__str__() + f', radius = {self.__radius}'