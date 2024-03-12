from account import Account

class Bank:
    def __init__(self, name):
        self.__name = name
        self.__accounts = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    def add(self, acc):
        self.__accounts.append(acc)
    
    def withdraw(self, id, amount):
        acc = self.search(id)
        if not acc:
            print(f'Account with id {id} not found')
            return
        
        acc.withdraw(amount)
    
    def deposit(self, id, amount):
        acc = self.search(id)
        if not acc:
            print(f'Account with id {id} not found')
            return
        
        acc.deposit(amount)
    
    def search(self, id):
        for acc in self.__accounts:
            if acc.id == id:
                return acc
        return None