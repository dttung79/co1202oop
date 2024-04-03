from tkinter import *
from tkinter import messagebox as msb
from tkinter import filedialog
from base_gui import BaseGUI
from sport_store import SportStore
from sport_item import SportItem

class SportGUI(BaseGUI):
    def __init__(self):
        super().__init__('Sport Store', '400x200')
        self.store = SportStore()
        self.current = -1

    def create_widgets(self):
        lbl_store_view = Label(self.window, text='Store View')
        lbl_store_view.grid(row=0, column=1)

        self.btn_load = Button(self.window, text='Load', width=5, command=self.btn_load_clicked)
        self.btn_load.grid(row=0, column=5, sticky=E)

        lbl_item = Label(self.window, text='Item')
        lbl_item.grid(row=1, column=0)

        self.txt_item = Entry(self.window, width=35)
        self.txt_item.grid(row=1, column=1, columnspan=5)

        lbl_brand = Label(self.window, text='Brand')
        lbl_brand.grid(row=2, column=0)

        self.txt_brand = Entry(self.window, width=35)
        self.txt_brand.grid(row=2, column=1, columnspan=5)

        lbl_price = Label(self.window, text='Price')
        lbl_price.grid(row=3, column=0)

        self.txt_price = Entry(self.window, width=35)
        self.txt_price.grid(row=3, column=1, columnspan=5)

        self.btn_first = Button(self.window, text='|<', command=self.btn_first_clicked)
        self.btn_first.grid(row=4, column=1)

        self.btn_previous = Button(self.window, text='<<', command=self.btn_prev_clicked)
        self.btn_previous.grid(row=4, column=2)

        self.txt_id = Entry(self.window, width=5)
        self.txt_id.grid(row=4, column=3)
        self.txt_id.bind('<Return>', self.txt_id_enter)

        self.btn_next = Button(self.window, text='>>', command=self.btn_next_clicked)
        self.btn_next.grid(row=4, column=4)

        self.btn_last = Button(self.window, text='>|', command=self.btn_last_clicked)
        self.btn_last.grid(row=4, column=5)

    def btn_load_clicked(self):
        file_name = filedialog.askopenfilename()
        self.store.load_items(file_name)
        self.current = 0
        self.show_current_item()
    
    def btn_next_clicked(self):
        if self.current == len(self.store.get_names()) - 1:
            msb.showinfo('Info', 'This is the last item')
            return
        self.current += 1
        self.show_current_item()
    
    def btn_prev_clicked(self):
        if self.current == 0:
            msb.showinfo('Info', 'This is the first item')
            return
        self.current -= 1
        self.show_current_item()
    
    def btn_first_clicked(self):
        self.current = 0
        self.show_current_item()
    
    def btn_last_clicked(self):
        self.current = len(self.store.get_names()) - 1
        self.show_current_item()

    def txt_id_enter(self, event):
        id = self.txt_id.get()
        index = self.store.search_id(id)
        if index == None:
            msb.showerror('Error', 'ID not found')
            return
        self.current = index
        self.show_current_item()

    def show_current_item(self):
        id, name, brand, price = self.store.get_item(self.current)
        self.set_text(self.txt_id, id)
        self.set_text(self.txt_item, name)
        self.set_text(self.txt_brand, brand)
        self.set_text(self.txt_price, price)

    def set_text(self, txt_widget, text):
        txt_widget.delete(0, END)
        txt_widget.insert(0, text)

if __name__ == '__main__':
    gui = SportGUI()
    gui.run()