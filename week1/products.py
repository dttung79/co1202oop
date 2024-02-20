# declare global lists to store product information
ids = [1, 2, 3, 4, 5]
names = ["T-Shirt", "Sweater", "Jeans", "Skirt", "Dress"]
prices = [20, 25, 30, 15, 40]

def main():
    running = True
    while running:
        print_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_product()
        elif choice == 2:
            edit_product()
        elif choice == 3:
            delete_product()
        elif choice == 4:
            show_all()
        elif choice == 5:
            print('Goodbye!')
            running = False
        else:
            print('Invalid choice!')

def print_menu():
    print("PRODUCT MANAGEMENT SYSTEM")
    print("1. Add product")
    print("2. Edit product")
    print("3. Delete product")
    print("4. Show all products")
    print("5. Exit")

def add_product():
    print('Add new product')
    id = int(input('Enter product id: '))
    ids.append(id)

    name = input('Enter product name: ')
    names.append(name)

    price = int(input('Enter product price: '))
    prices.append(price)

    print('Product added successfully!')

def edit_product():
    id = int(input('Enter product id to edit: '))
    found = search_product(id)

    if found == -1:
        print('Product not found!')
        return  # exit the function
    
    new_price = int(input('Enter new price: '))
    prices[found] = new_price # update the price
    print('Product updated successfully!')

def delete_product():
    id = int(input('Enter product id to delete: '))
    found = search_product(id)

    if found == -1:
        print('Product not found!')
        return  # exit the function
    
    ids.pop(found)
    names.pop(found)
    prices.pop(found)

    print('Product deleted successfully!')
    
def search_product(id):
    for i in range(len(ids)):
        if ids[i] == id:    # if found the id
            return id
    return -1

def show_all():
    print('All products')
    print(f'{"ID":<5} | {"Name":<10} | {"Price":<10}')
    for i in range(len(ids)):
        print(f'{ids[i]:<5} | {names[i]:<10} | {prices[i]:<10}')

#### main program starts here
if __name__ == "__main__":
    main()