from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, id, name, balance):
        self._id = id
        self._name = name
        self._balance = balance
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def balance(self):
        return self._balance
    
    @abstractmethod
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        self._balance += amount
        print(f'Deposit ${amount} to account id {self._id} successfully')
        print(f'Current balance: ${self._balance}')
    
    def __str__(self):
        return f'ID: {self._id}, Name: {self._name}, Balance: {self._balance}'