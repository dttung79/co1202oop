from abc import ABC, abstractmethod

# Shape is an abstract class which has at least 1 abstract method
class Shape(ABC):
    def __init__(self, name):
        self._name = name # protected attribute
        self._type = 'Shape' # protected attribute
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def type(self):
        return self._type

    @abstractmethod
    def area(self):       # area is an abstract method, no implementation
        pass

    def __str__(self) -> str:
        return f'{self._type} {self._name}'
    
# s = Shape('shape') --- cannot create object from abstract class !!!