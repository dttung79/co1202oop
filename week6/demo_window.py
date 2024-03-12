from tkinter import *
from tkinter import messagebox

class MyWindow:
    def __init__(self):
        self.window = Tk() # create a window
        self.window.title("Hello GUI") # set the title of the window
        self.window.geometry('500x300') # set the size of the window

        self.init_widgets() # create and place widgets in the window

    def init_widgets(self):
        self.lbl_hello = Label(self.window, text="Hello World!") # create a label
        self.lbl_hello.grid(column=0, row=0) # place the label in the window

        self.lbl_python = Label(self.window, text="I love Python!") # create a label
        self.lbl_python.grid(column=1, row=1) # place the label in the window

        # create a button, register a callback function to the button (or event handler)
        self.btn_OK = Button(self.window, text="OK", command=self.btn_OK_clicked) 
        self.btn_OK.grid(column=2, row=2) # place the button in the window

    def btn_OK_clicked(self):
        messagebox.showinfo('Hello', 'Hello Python!')
    
    def run(self):
        self.window.mainloop()

# run the window
if __name__ == "__main__":
    my_window = MyWindow()
    my_window.run()