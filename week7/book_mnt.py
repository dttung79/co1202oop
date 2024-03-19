from tkinter import *
from tkinter import messagebox as msb
from book import Book
from book_lib import BookLib

class BookManagement():
    def __init__(self):
        self.booklib = BookLib()
        self.window = self.create_window()
        self.create_widgets()

        self.fill_titles()
    
    def create_window(self):
        window = Tk()
        window.title('Book Management')
        window.geometry('600x300')
        return window
    
    def create_widgets(self):
        self.lbl_all_books = Label(self.window, text='List of all books')
        self.lbl_all_books.grid(row=0, column=0, sticky=W)

        self.lst_books = Listbox(self.window, width=30, height=10, exportselection=0)
        self.lst_books.grid(row=1, column=0, sticky=W, rowspan=5)
        # bind event
        self.lst_books.bind('<<ListboxSelect>>', self.on_select)

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

        self.btn_add = Button(self.window, text='Add', command=self.add_book)
        self.btn_add.grid(row=5, column=2, sticky=E)

        self.btn_update = Button(self.window, text='Update', command=self.update_book)
        self.btn_update.grid(row=5, column=3, sticky=E)

        self.btn_delete = Button(self.window, text='Delete', command=self.delete_book)
        self.btn_delete.grid(row=5, column=4, sticky=E)
    
    def delete_book(self):
        # get selected index
        index = self.lst_books.curselection()
        if len(index) == 0:
            msb.showwarning('Warning', 'Please select a book to delete')
            return
        
        index = index[0]
        # delete the book from the booklib
        self.booklib.delete_book(index)
        # delete the book from the listbox
        self.lst_books.delete(index)
        msb.showinfo('Success', 'Book deleted successfully')
        
    def update_book(self):
        # get selected index
        index = self.lst_books.curselection()
        if len(index) == 0:
            msb.showwarning('Warning', 'Please select a book to update')
            return
        
        index = index[0]
        # get book information from textboxes
        id = self.txt_id.get()
        title = self.txt_title.get()
        author = self.txt_author.get()
        price = self.txt_price.get()
        try:
            # update the book in the booklib
            self.booklib.update_book(index, title, author, float(price))
            # update the book in the listbox
            self.lst_books.delete(index)
            self.lst_books.insert(index, title)
            msb.showinfo('Success', 'Book updated successfully')
        except ValueError as e:
            msb.showerror('Error', e)

    def add_book(self):
        # get book information from textboxes
        id = self.txt_id.get()
        title = self.txt_title.get()
        author = self.txt_author.get()
        price = self.txt_price.get()

        try:
            # create a book object
            book = Book(int(id), title, author, float(price))
            # add the book to the booklib
            self.booklib.add_book(book)
            # add the book to the listbox
            self.lst_books.insert(END, title)

            msb.showinfo('Success', 'Book added successfully')
        except ValueError as e:
            msb.showerror('Error', e)

    def fill_titles(self):
        # get titles from booklib
        titles = self.booklib.get_titles()
        # add titles to the listbox
        for title in titles:
            self.lst_books.insert(END, title)

    def on_select(self, event):
        # get selected index
        sel_index = self.lst_books.curselection()
        if len(sel_index) == 0:
            return
        sel_index = sel_index[0]

        # get book information
        id, title, author, price = self.booklib.get_book(sel_index)
        # display book information
        self.txt_id.delete(0, END)
        self.txt_id.insert(END, id)
        self.txt_title.delete(0, END)
        self.txt_title.insert(END, title)
        self.txt_author.delete(0, END)
        self.txt_author.insert(END, author)
        self.txt_price.delete(0, END)
        self.txt_price.insert(END, price)

    def run(self):
        self.window.mainloop()  

if __name__ == '__main__':
    program = BookManagement()
    program.run()