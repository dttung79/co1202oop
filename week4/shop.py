from item import Item
from inventory import Inventory

class Shop:
    def __init__(self):
        self.__inventory = Inventory()
    
    def run(self):
        while True:
            self.__print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1: self.__add_new_item()
            elif choice == 2: self.__add_item()
            elif choice == 3: self.__remove_item()
            elif choice == 4: self.__remove_old_item()
            elif choice == 5: self.__show_most_expensive()
            elif choice == 6: self.__show_total_storage()
            elif choice == 7: print('Goodbye!'); break
            else: print('Invalid choice!')
    
    def __print_menu(self):
        print("SHOP MANAGEMENT SYSTEM")
        print("1. Add new item")
        print("2. Add item")
        print("3. Remove item")
        print("4. Remove old item")
        print("5. Show most expensive item")
        print("6. Show total storage")
        print("7. Quit")

    def __add_new_item(self):
        id = int(input('Enter item ID: '))
        name = input('Enter item name: ')
        price = float(input('Enter item price: '))
        quantity = int(input('Enter item quantity: '))
        i = Item(id, name, price, quantity)
        self.__inventory.add_new(i)
    
    def __add_item(self):
        id = int(input('Enter item ID to add: '))
        amount = int(input('Enter amount to add: '))
        self.__inventory.add(id, amount)
    
    def __remove_item(self):
        id = int(input('Enter item ID to remove: '))
        amount = int(input('Enter amount to remove: '))
        self.__inventory.remove(id, amount)
    
    def __remove_old_item(self):
        id = int(input('Enter item ID to remove: '))
        self.__inventory.remove_old(id)
    
    def __show_most_expensive(self):
        max_item = self.__inventory.most_expensive()
        print(f'Most expensive item: {max_item.name}, price = ${max_item.price}')
    
    def __show_total_storage(self):
        total = self.__inventory.total_storage()
        print(f'Total storage: {total}')
    

#### Main Program ####
if __name__ == "__main__":
    s = Shop()
    s.run()
