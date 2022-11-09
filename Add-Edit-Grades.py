'''
Title: Add/Edit Grades in LMS
Author: Gabrielle Knapp
Date: 11/9/2022

Goal: Allow users to add new grades to previously uploaded data or to edit a grade from data previously uploaded

'''
from tkinter import *
window=Tk()
btn1=Button(window, text="Apply", fg='blue')
btn1.place(x=100, y=175)
btn2=Button(window, text="Return to Main", fg='blue')
btn2.place(x=145, y=175)
lbl1=Label(window, text="Assignment Title: ", fg='black', font=("Helvetica", 8))
lbl1.place(x=0, y=100)
lbl1=Label(window, text="Grade: ", fg='black', font=("Helvetica", 8))
lbl1.place(x=0, y=125)
lbl1=Label(window, text="Add/Edit/Rename: ", fg='black', font=("Helvetica", 8))
lbl1.place(x=0, y=150)
lbl=Label(window, text="Add/Edit Grades", fg='red', font=("Helvetica", 11))
lbl.place(x=100, y=50)
txtfld1=Entry(window, text="Assignment Title: ", bd=5)
txtfld1.place(x=100, y=100)
txtfld2=Entry(window, text="Grade: ", bd=5)
txtfld2.place(x=100, y=125)
txtfld3=Entry(window, text="Add/Edit/Rename: ", bd=5)
txtfld3.place(x=100, y=150)
window.title('Add/Edit Grades')
window.geometry("300x200+20+20")
window.mainloop()
