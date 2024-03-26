from sport_item import SportItem
import csv


class SportStore:
    def __init__(self):
        self.__items = []

    def load_items(self, file_name):
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                self.__items.append(SportItem(row[0], row[1], row[2], row[3]))
    
    def get_names(self):
        return [item.name for item in self.__items]

    def get_item(self, index):
        if index < 0 or index >= len(self.__items):
            raise ValueError('Index out of range')
        item = self.__items[index]
        return item.id, item.name, item.branch, item.price
    
    def update_item(self, index, new_name, new_branch, new_price):
        if index < 0 or index >= len(self.__items):
            raise ValueError('Index out of range')
        item = self.__items[index]
        item.name = new_name
        item.branch = new_branch
        item.price = new_price
    
    def add_item(self, id, name, branch, price):
        item = SportItem(id, name, branch, price)
        self.__items.append(item)

    def remove_item(self, index):
        if index < 0 or index >= len(self.__items):
            raise ValueError('Index out of range')
        del self.__items[index]
    
    def save_items(self, file_name):
        with open(file_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Item Name', 'Branch', 'Price'])
            for item in self.__items:
                writer.writerow([item.id, item.name, item.branch, item.price])