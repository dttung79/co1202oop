from normal_account import NormalAccount
from debit_account import DebitAccount
from bank import Bank

class BankProgram():
    def __init__(self):
        self.__bank = Bank('Vietcom Bank')
    
    def run(self):
        while True:
            self.__print_menu()
            choice = int(input('Enter your choice: '))
            if   choice == 1:   self.__add_account()
            elif choice == 2:   self.__withdraw()
            elif choice == 3:   self.__deposit()
            elif choice == 4:   break
            else: print('Invalid choice!')
        
        print('Program ended')
    
    def __print_menu(self):
        print(f"{self.__bank.name} MANAGEMENT SYSTEM")
        print("1. Add account")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Quit")
    
    def __add_account(self):
        acc_type = input('Enter account type (normal/debit): ')
        id = int(input('Enter account ID: '))
        name = input('Enter account name: ')
        balance = float(input('Enter account balance: '))

        if acc_type == 'normal':
            self.__bank.add(NormalAccount(id, name, balance))
        else:
            debit = float(input('Enter debit amount: '))
            self.__bank.add(DebitAccount(id, name, balance, debit))
    
    def __withdraw(self):
        id = int(input('Enter account ID: '))
        amount = float(input('Enter amount to withdraw: '))
        self.__bank.withdraw(id, amount)
    
    def __deposit(self):
        id = int(input('Enter account ID: '))
        amount = float(input('Enter amount to deposit: '))
        self.__bank.deposit(id, amount)

# Main Program
program = BankProgram()
program.run()