'''
Title: Finalization Screen
Author: Gabrielle Knapp
Date: 11/9/2022

Goal: Provide a screen for users when they are about to finalize their settings

Widgets:
window--> window storing all of the gui
btn1--> button displaying 'finalize', allowing users the opportunity to continue
btn2--> button displaying 'cancel', allowing users the opportunity to cancel
lbl1--> label describing situation and options to the users
'''
from tkinter import *
window=Tk()
btn1=Button(window, text="Finalize", fg='red')
btn1.place(x=100, y=175)
btn2=Button(window, text="Cancel", fg='red')
btn2.place(x=150, y=175)
lbl1=Label(window, text="Once finalized, this cannot be changed.", fg='black', font=("Helvetica", 12))
lbl1.place(x=0, y=100)
window.title('Finalize Screen')
window.geometry("300x200+20+20")
window.mainloop()