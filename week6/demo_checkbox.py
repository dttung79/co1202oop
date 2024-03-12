from tkinter import *
from tkinter import messagebox

### EVENT HANDLER ###
def chk_item_checked():
    total = 0
    if tshirt_checked.get() == True:
        total += 20
    if jeans_checked.get() == True:
        total += 50
    if shoes_checked.get() == True:
        total += 80
    lbl_payment['text'] = 'Payment: $' + str(total)

### CREATE WINDOW & WIDGETS ###
window = Tk()
window.geometry('300x200')
window.title('Demo Checkbox')

lbl_cart = Label(window, text='Shopping Cart')
lbl_cart.grid(row=0, column=0)

tshirt_checked = BooleanVar()
chk_tshirt = Checkbutton(window, text='T-shirt ($20)', \
                            variable=tshirt_checked, command=chk_item_checked)
chk_tshirt.grid(row=1, column=0, sticky=W)

jeans_checked = BooleanVar()
chk_jeans = Checkbutton(window, text='Jeans ($50)', \
                            variable=jeans_checked, command=chk_item_checked)
chk_jeans.grid(row=2, column=0, sticky=W)

shoes_checked = BooleanVar()
chk_shoes = Checkbutton(window, text='Shoes ($80)', \
                            variable=shoes_checked, command=chk_item_checked)
chk_shoes.grid(row=3, column=0, sticky=W)

lbl_payment = Label(window, text='Payment :$0')
lbl_payment.grid(row=4, column=0)

#### MAIN LOOP ####
window.mainloop() # create an event loop listening to events