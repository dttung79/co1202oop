class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @property
    def quantity(self):
        return self.__quantity
    
    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price
    
    @quantity.setter
    def quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.__quantity = quantity
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty")
        self.__name = name
    
    def show(self):
        print(f'Name: {self.__name}, Price: {self.__price}, Quantity: {self.__quantity}')

    def total_value(self):
        return self.__price * self.__quantity