from tkinter import *
from tkinter import messagebox

#### EVENT HANDLERS ####
def btn_answer_clicked():
    answer = answer_selected.get() # get which radio button is selected
    
    if answer == 3: # correct answer (Mark Zuckerberg)
        messagebox.showinfo('Result', 'Correct!')
    else:
        messagebox.showerror('Result', 'Wrong!')

#### CREATE WINDOW & WIDGETS ####
window = Tk()
window.geometry('350x200')
window.title('Demo Radio')

answer_selected = IntVar() # variable to bind to radio buttons

lbl_quiz = Label(window, text='Quiz: Who is CEO of Facebook?')
lbl_quiz.grid(row=0, column=0)

rd_choice1 = Radiobutton(window, text='Steve Jobs', value=1, variable=answer_selected)
rd_choice1.grid(row=1, column=1, sticky=W)

rd_choice2 = Radiobutton(window, text='Bill Gates', value=2, variable=answer_selected)
rd_choice2.grid(row=2, column=1, sticky=W)

rd_choice3 = Radiobutton(window, text='Mark Zuckerberg', value=3, variable=answer_selected)
rd_choice3.grid(row=3, column=1, sticky=W)

rd_choice4 = Radiobutton(window, text='Jeff Bezos', value=4, variable=answer_selected)
rd_choice4.grid(row=4, column=1, sticky=W)

btn_answer = Button(window, text='Answer', width=6, command=btn_answer_clicked)
btn_answer.grid(row=5, column=1, sticky=W)

### MAIN LOOP ###
window.mainloop() # create an event loop