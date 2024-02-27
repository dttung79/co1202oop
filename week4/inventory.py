from item import Item
class Inventory:
    def __init__(self):
        self.__items = []
    
    def add_new(self, new_item):
        self.__items.append(new_item)
        print(f'Item {new_item.name} has been added.')
    
    def __search_id(self, id):
        for item in self.__items:
            if item.id == id:
                return item
        return None
    
    def add(self, item_id, amount):
        # search for item with the given id
        found_item = self.__search_id(item_id)
        if found_item == None:
            print(f'Item with ID {item_id} not found.')
        else:
            found_item.add_quantity(amount)
            print(f'{amount} {found_item.name} has been added.')
    
    def remove_old(self, item_id):
        found_item = self.__search_id(item_id)
        if not found_item:
            print(f'Item with ID {item_id} not found.')
        else:
            self.__items.remove(found_item)
            print(f'Item {found_item.name} has been removed.')
    
    def remove(self, item_id, amount):
        found_item = self.__search_id(item_id)
        if not found_item:
            print(f'Item with ID {item_id} not found.')
        else:
            found_item.remove_quantity(amount)
            print(f'{amount} {found_item.name} has been removed.')
    
    def most_expensive(self):
        max_item = self.__items[0]
        for item in self.__items:
            if item.price > max_item.price:
                max_item = item
        
        return max_item
    
    def total_storage(self):
        total = 0
        for item in self.__items:
            total += item.quantity
        
        return total