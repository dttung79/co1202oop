from tkinter import *
from tkinter import messagebox as msb
from book import Book
from book_lib import BookLib

class BookManagement():
    def __init__(self):
        self.booklib = BookLib()
        self.window = self.create_window()
        self.create_widgets()
    
    def create_window(self):
        window = Tk()
        window.title('Book Management')
        window.geometry('600x300')
        return window
    
    def create_widgets(self):
        self.lbl_all_books = Label(self.window, text='List of all books')
        self.lbl_all_books.grid(row=0, column=0, sticky=W)

        self.lst_books = Listbox(self.window, width=30, height=10)
        self.lst_books.grid(row=1, column=0, sticky=W, rowspan=5)

        self.lbl_id = Label(self.window, text='ID')
        self.lbl_id.grid(row=1, column=1, sticky=E)

        self.txt_id = Entry(self.window, width=25)
        self.txt_id.grid(row=1, column=2, columnspan=3, sticky=W)

        self.lbl_title = Label(self.window, text='Title')
        self.lbl_title.grid(row=2, column=1, sticky=E)

        self.txt_title = Entry(self.window, width=25)
        self.txt_title.grid(row=2, column=2, columnspan=3, sticky=W)

        self.lbl_author = Label(self.window, text='Author')
        self.lbl_author.grid(row=3, column=1, sticky=E)

        self.txt_author = Entry(self.window, width=25)
        self.txt_author.grid(row=3, column=2, columnspan=3, sticky=W)

        self.lbl_price = Label(self.window, text='Price')
        self.lbl_price.grid(row=4, column=1, sticky=E)

        self.txt_price = Entry(self.window, width=25)
        self.txt_price.grid(row=4, column=2, columnspan=3, sticky=W)

        self.btn_add = Button(self.window, text='Add')
        self.btn_add.grid(row=5, column=2, sticky=E)

        self.btn_update = Button(self.window, text='Update')
        self.btn_update.grid(row=5, column=3, sticky=E)

        self.btn_delete = Button(self.window, text='Delete')
        self.btn_delete.grid(row=5, column=4, sticky=E)

    
    def run(self):
        self.window.mainloop()  

if __name__ == '__main__':
    program = BookManagement()
    program.run()