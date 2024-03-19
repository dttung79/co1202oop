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

    