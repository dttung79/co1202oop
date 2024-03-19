class Book:
    def __init__(self, id, title, author, price):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__price = price
    
    @property
    def id(self):
        return self.__id
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if value == '':
            raise ValueError('Title cannot be empty')
        self.__title = value

    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, value):
        if value == '':
            raise ValueError('Author cannot be empty')
        self.__author = value
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative')
        self.__price = value