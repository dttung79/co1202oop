from sport_item import SportItem
from sport_store import SportStore
from tkinter import *
from tkinter import messagebox as msb
from tkinter import filedialog

class StoreGUI:
    def __init__(self):
        self.store = SportStore()
        self.window = self.create_window()
        self.create_widgets()
    
    def create_window(self):
        window = Tk()
        window.title('Sport Store')
        window.geometry('600x400')
        return window
    
    def create_widgets(self):
        lbl_items = Label(self.window, text='Items')
        lbl_items.grid(row=0, column=0, sticky=W)

        self.lst_items = Listbox(self.window, width=30)
        self.lst_items.grid(row=1, column=0, rowspan=5, columnspan=2, sticky=W)

        lbl_id = Label(self.window, text='ID')
        lbl_id.grid(row=1, column=3, sticky=W)

        self.txt_id = Entry(self.window, width=25)
        self.txt_id.grid(row=1, column=4, columnspan=3, sticky=W)

        lbl_name = Label(self.window, text='Name')
        lbl_name.grid(row=2, column=3, sticky=W)

        self.txt_name = Entry(self.window, width=25)
        self.txt_name.grid(row=2, column=4, columnspan=3, sticky=W)

        lbl_brand = Label(self.window, text='Brand')
        lbl_brand.grid(row=3, column=3, sticky=W)

        self.txt_brand = Entry(self.window, width=25)
        self.txt_brand.grid(row=3, column=4, columnspan=3, sticky=W)

        lbl_price = Label(self.window, text='Price')
        lbl_price.grid(row=4, column=3, sticky=W)

        self.txt_price = Entry(self.window, width=25)
        self.txt_price.grid(row=4, column=4, columnspan=3, sticky=W)

        btn_add = Button(self.window, width=5, text='Add')
        btn_add.grid(row=5, column=4, sticky=W)

        btn_update = Button(self.window, width=5, text='Update')
        btn_update.grid(row=5, column=5, sticky=W)

        btn_delete = Button(self.window, width=5, text='Delete')
        btn_delete.grid(row=5, column=6, sticky=W)

        btn_load = Button(self.window, width=5, text='Load', command=self.btn_load_clicked)
        btn_load.grid(row=6, column=0, sticky=E)

        btn_save = Button(self.window, width=5, text='Save', command=self.btn_save_clicked)
        btn_save.grid(row=6, column=1, sticky=W)
    
    def btn_save_clicked(self):
        # open file dialog to select file
        file_name = filedialog.askopenfilename()
        try:
            # save items to file
            self.store.save_items(file_name)
            msb.showinfo('Info', 'Items saved to file')
        except Exception as e:
            msb.showerror('Error', str(e))

    def btn_load_clicked(self):
        # open file dialog to select file
        file_name = filedialog.askopenfilename()
        
        try:
            # load items from file
            self.store.load_items(file_name)
            # fill item names into listbox
            self.fill_names()
        
        except Exception as e:
            msb.showerror('Error', str(e))
    
    def fill_names(self):
        # get names list from store
        names = self.store.get_names()
        # clear listbox
        self.lst_items.delete(0, END)
        # insert names to listbox
        for name in names:
            self.lst_items.insert(END, name)

    
    def run(self):
        self.window.mainloop()

###
program = StoreGUI()
program.run()