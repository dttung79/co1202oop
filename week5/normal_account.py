from account import Account

class NormalAccount(Account):
    def __init__(self, id, name, balance):
        super().__init__(id, name, balance)
    
    def withdraw(self, amount):
        if amount > self._balance:
            print(f'Not enough balance to withdraw ${amount}')
            return
        
        self._balance -= amount
        print(f'Withdraw ${amount} from account id {self._id} successfully')
        print(f'Current balance: ${self._balance}')
        