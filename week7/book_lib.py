from book import Book
import csv

class BookLib:
    def __init__(self):
        self.__books = []
        with open('books.csv', 'r') as f:    # Open the file f
            csvreader = csv.reader(f)        # Create a csv reader object from f   
            # skip the header
            next(csvreader)
            for row in csvreader:            # for each row in the file
                id = int(row[0])
                title = row[1]
                author = row[2]
                price = float(row[3])
                book = Book(id, title, author, price) # create a Book object
                self.__books.append(book)             # add the book to the list
    
    def get_titles(self):
        return [book.title for book in self.__books]
    
    def get_book(self, i):
        book = self.__books[i]
        return book.id, book.title, book.author, book.price
    
    def update_book(self, i, title, author, price):
        book = self.__books[i] # get the book at index i
        # change the book's information
        book.title = title
        book.author = author
        book.price = price

    def add_book(self, b):
        self.__books.append(b)