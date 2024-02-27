class Item:
    def __init__(self, id, name, price, quantity):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value != "":
            self.__name = value
        else:
            print("Item name cannot be empty")
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            print("Price cannot be negative")
    
    @property
    def quantity(self):
        return self.__quantity
    
    def add_quantity(self, value):
        if value > 0:
            self.__quantity += value
        else:
            print("Quantity must be positive")
    
    def remove_quantity(self, value):
        if value > 0 and value <= self.__quantity:
            self.__quantity -= value
        else:
            print("Invalid quantity")