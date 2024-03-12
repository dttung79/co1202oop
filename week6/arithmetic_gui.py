from tkinter import *
from tkinter import messagebox

#### EVENT HANDLER ####
def btn_add_clicked():
    do_arithmetic_operator('+')

def btn_sub_clicked():
    do_arithmetic_operator('-')

def btn_div_clicked():
    do_arithmetic_operator('/')

def do_arithmetic_operator(operator):
    a = float(txt_a.get()) # get content of text box a
    b = float(txt_b.get()) # get content of text box b
    if operator == '+':
        c = a + b
    elif operator == '-':
        c = a - b
    elif operator == '/':
        if b == 0.0:
            messagebox.showerror('Error', 'Cannot divide by zero!')
            return
        else:
            c = a / b
    
    lbl_result['text'] = str(c) # change the text of label lbl_result

#### CREATE WINDOW & WIDGETS ####
window = Tk()
window.geometry('300x200')
window.title('Arithmetic GUI')

lbl_a = Label(window, text='a = ')
lbl_a.grid(row=0, column=0)

txt_a = Entry(window, width=10)
txt_a.grid(row=0, column=1, sticky=W)

lbl_b = Label(window, text='b = ')
lbl_b.grid(row=1, column=0)

txt_b = Entry(window, width=10)
txt_b.grid(row=1, column=1, sticky=W)

lbl_c = Label(window, text='c = ')
lbl_c.grid(row=2, column=0)

lbl_result = Label(window, text='0')
lbl_result.grid(row=2, column=1, sticky=W)

btn_add = Button(window, text='Add', width=6, command=btn_add_clicked)
btn_add.grid(row=3, column=1, sticky=W)

btn_sub = Button(window, text='Subtract', width=6, command=btn_sub_clicked)
btn_sub.grid(row=4, column=1, sticky=W)

btn_div = Button(window, text='Divide', width=6, command=btn_div_clicked)
btn_div.grid(row=5, column=1, sticky=W)

#### MAIN LOOP ####
window.mainloop()