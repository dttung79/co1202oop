from account import Account

class DebitAccount(Account):
    def __init__(self, id, name, balance, debit):
        super().__init__(id, name, balance)
        self._debit = debit

    @property
    def debit(self):
        return self._debit
    
    @debit.setter
    def debit(self, debit):
        self._debit = debit
    
    def withdraw(self, amount):
        if amount > self._balance + self._debit:
            print(f'Not enough balance to withdraw ${amount}')
            return
        
        self._balance -= amount
        print(f'Withdraw ${amount} from account id {self._id} successfully')
        print(f'Current balance: ${self._balance}')
    
    def __str__(self):
        return super().__str__() + f', Debit litmit: ${self._debit}'