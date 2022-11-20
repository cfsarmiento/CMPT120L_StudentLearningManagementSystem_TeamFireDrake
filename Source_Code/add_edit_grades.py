'''
Title: Add/Edit Grades
Window: Add/Edit Grades Window
Author: Gabrielle Knapp
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Allow users to input grades they wish to add or change to the system
Widgets: labels, textfields, and buttons
Other Requirements: TKInter for Interface Design.
'''
from tkinter import *
def ADD_EDIT_GRADES():
    window=Tk()
    window.configure(bg='grey')
    btn1=Button(window, text="Finalize", bg='grey', fg='white',font=("Helvetica 10 bold"))
    btn1.place(x=230, y=175)
    lbl1=Label(window, text="Assignment Title: ", bg='grey', fg='white', font=("Helvetica 12 bold"))
    lbl1.place(x=0, y=100)
    lbl1=Label(window, text="Grade: ", bg='grey', fg='white', font=("Helvetica 12 bold"))
    lbl1.place(x=0, y=125)
    lbl1=Label(window, text="Add/Edit/Rename: ", bg='grey', fg='white', font=("Helvetica 12 bold"))
    lbl1.place(x=0, y=150)
    lbl=Label(window, text="Add/Edit Grades", bg= 'grey', fg='white', font=("Helvetica 12 bold"))
    lbl.place(x=100, y=50)
    txtfld1=Entry(window, text="Assignment Title: ", bd=5)
    txtfld1.place(x=150, y=100)
    txtfld2=Entry(window, text="Grade: ", bd=5)
    txtfld2.place(x=150, y=125)
    txtfld3=Entry(window, text="Add/Edit/Rename: ", bd=5)
    txtfld3.place(x=150, y=150)
    window.title('Add/Edit Grades')
    window.geometry("300x200+20+20")
    window.mainloop()