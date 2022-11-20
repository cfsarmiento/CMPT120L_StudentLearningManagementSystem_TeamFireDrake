#Title: Student Learning Management System
#Window: Class Management System
#Authors: Cody Carruthers and Gabrielle Knapp
#Class: CMPT120L
#Professor: Reza Sadeghi
#Goal: Prints the classes, homework, weights, grades for the student
#Other Requirements: TKInter for Interface Design.
from tkinter import *
def CLASS_MANAGER():
    import tkinter as tk

    window=Tk()
    window.title('Class Manager')
    window.geometry('1000x300')
    window.configure(bg='grey')

    #Create a canvas object
    canvas=Canvas(window, width= 170, height= 50, bg="grey")
    canvas2=Canvas(window, width= 70, height= 50, bg="grey")
    canvas3=Canvas(window, width= 120, height= 50, bg="grey")
    canvas4=Canvas(window, width= 85, height= 50, bg="grey")
    canvas5=Canvas(window, width= 170, height= 50, bg="grey")
    canvas6=Canvas(window, width= 170, height= 50, bg="grey")
    canvas7=Canvas(window, width= 170, height= 50, bg="grey")
    canvas8=Canvas(window, width= 170, height= 50, bg="grey")
    canvas9=Canvas(window, width= 70, height= 50, bg="grey")
    canvas10=Canvas(window, width= 70, height= 50, bg="grey")
    canvas11=Canvas(window, width= 70, height= 50, bg="grey")
    canvas12=Canvas(window, width= 70, height= 50, bg="grey")
    canvas13=Canvas(window, width= 120, height= 50, bg="grey")
    canvas14=Canvas(window, width= 120, height= 50, bg="grey")
    canvas15=Canvas(window, width= 120, height= 50, bg="grey")
    canvas16=Canvas(window, width= 120, height= 50, bg="grey")
    canvas17=Canvas(window, width= 85, height= 50, bg="grey")
    canvas18=Canvas(window, width= 85, height= 50, bg="grey")
    canvas19=Canvas(window, width= 85, height= 50, bg="grey")
    canvas20=Canvas(window, width= 85, height= 50, bg="grey")


    #Add a text in Canvas
    canvas.create_text(80,25, text="Assignment Type", fill="white", font=('Helvetica 12 bold'))
    canvas.grid(row=0,column=0)

    canvas2.create_text(25,25, text="Grade", fill="white", font=('Helvetica 12 bold'))
    canvas2.grid(row=0, column=1)

    canvas3.create_text(50,25, text="Due Date", fill="white", font=('Helvetica 12 bold'))
    canvas3.grid(row=0, column=2)

    canvas4.create_text(30,25, text="Weight", fill="white", font=('Helvetica 12 bold'))
    canvas4.grid(row=0, column=3)

    canvas5.create_text(85,25, text="Assignment Type #1", fill="white", font=('Helvetica 12 bold'))
    canvas5.grid(row=1, column=0)

    canvas6.create_text(85,25, text="Assignment Type #2", fill="white", font=('Helvetica 12 bold'))
    canvas6.grid(row=2, column=0)

    canvas7.create_text(85,25, text="Assignment Type #3", fill="white", font=('Helvetica 12 bold'))
    canvas7.grid(row=3, column=0)

    canvas8.create_text(85,25, text="Assignment Type #4", fill="white", font=('Helvetica 12 bold'))
    canvas8.grid(row=4, column=0)

    canvas9.create_text(35,25, text="Grade #1", fill="white", font=('Helvetica 12 bold'))
    canvas9.grid(row=1, column=1)

    canvas10.create_text(35,25, text="Grade #2", fill="white", font=('Helvetica 12 bold'))
    canvas10.grid(row=2, column=1)

    canvas11.create_text(35,25, text="Grade #3", fill="white", font=('Helvetica 12 bold'))
    canvas11.grid(row=3, column=1)

    canvas12.create_text(35,25, text="Grade #4", fill="white", font=('Helvetica 12 bold'))
    canvas12.grid(row=4, column=1)

    canvas13.create_text(55,25, text="Due Date #1", fill="white", font=('Helvetica 12 bold'))
    canvas13.grid(row=1, column=2)

    canvas14.create_text(55,25, text="Due Date #2", fill="white", font=('Helvetica 12 bold'))
    canvas14.grid(row=2, column=2)

    canvas15.create_text(55,25, text="Due Date #3", fill="white", font=('Helvetica 12 bold'))
    canvas15.grid(row=3, column=2)

    canvas16.create_text(55,25, text="Due Date #4", fill="white", font=('Helvetica 12 bold'))
    canvas16.grid(row=4, column=2)

    canvas17.create_text(40,25, text="Weight #1", fill="white", font=('Helvetica 12 bold'))
    canvas17.grid(row=1, column=3)

    canvas18.create_text(40,25, text="Weight #2", fill="white", font=('Helvetica 12 bold'))
    canvas18.grid(row=2, column=3)

    canvas19.create_text(40,25, text="Weight #3", fill="white", font=('Helvetica 12 bold'))
    canvas19.grid(row=3, column=3)

    canvas20.create_text(40,25, text="Weight #4", fill="white", font=('Helvetica 12 bold'))
    canvas20.grid(row=4, column=3)

    window.mainloop()