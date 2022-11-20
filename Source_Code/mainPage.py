'''
Title: Add Class
Window: Add Class Window
Author: Ethan Morton
Class: CMPT120L
Professor: Reza Sadeghi
Goal: 
Widgets: 
Other Requirements: TKInter for Interface Design.
'''
import tkinter as tk
from tkinter import *
import os
import pathlib
#os.chdir(pathlib.Path(__file__).parent.resolve())  # we need to create a folder for each semester so that I can use that directory to open the files
window=tk.Tk()
window.title("Main Page")
window.geometry("1550x550")
window.config(bg="Gray")

frame1=tk.Frame(window,bg="Gray",highlightbackground="White",highlightthickness=1,width=100,height=100)
frame1.grid(row=0,column=0)
tk.Label(window,bg="Gray",fg="White",text="SLMS",font='Helvetica 30 bold').grid(row=0,column=0)

frame2=tk.Frame(window,bg="Gray",width=500,height=140)
frame2.grid(row=0,column=1)
label= tk.Label(bg="Gray", fg="White", text="Course Name:       Grade:       Status:       ", font='Helvetica 12 bold').grid(row=0,column=1)
label= tk.Label(bg="Gray", fg="White", text="Semester GPA:    \nCummulative GPA:     ", font='Helvetica 12 bold').grid(row=0,column=2)

frame3=tk.Frame(window,bg="Gray",width=249,height=249)
frame3.grid(row=1,column=0)

#num=1
for i in range(1,9):    # instead of having range(1,9), this will get the number of classes and iterate through that. range(1,9) is just a placeholder
    tk.Button(frame3,bg="Gray",fg="White",text="Class "+str(i),font='Helvetica 12 bold').grid(row=3+i,column=0,pady=5)
    #num+=1

frame4=tk.Frame(window,bg="Gray",highlightbackground="White",highlightthickness=1,width=500,height=300)
frame4.grid(row=1,column=1)
#textBox1=Text(frame4, bg="Gray", fg="White").grid(row=1, column=0)
yearFrame = tk.Frame(frame4, bg = "Gray", width = 166, height = 300)
semesterFrame = tk.Frame(frame4, bg = "Gray", width = 166, height = 300)
gpaFrame = tk.Frame(frame4, bg = "Gray", width = 166, height = 300)

yearLabel = tk.Label(yearFrame, bg = "Gray", fg = "White", text = "Year", font = 'Helvetica 12 bold')
yearLabel.grid(row=0,column=0)

semesterLabel = tk.Label(semesterFrame, bg = "Gray", fg = "White", text = "Semester", font = 'Helvetica 12 bold')
semesterLabel.grid(row=0,column=0)

gpaLabel = tk.Label(gpaFrame, bg = "Gray", fg = "White", text = "GPA", font = 'Helvetica 12 bold')
gpaLabel.grid(row=0,column=0)

'''
Each semester should have its own folder, so I need to iterate through each folder
Within each folder, there should be a file with the semester information: year, session, GPA
They should be sorted in order of most recent at the top to oldest at the bottom
'''

frame5=tk.Frame(window,bg="Gray", width=500,height=300)
frame5.grid(row=1, column=2)
tk.Button(frame5,bg="Gray",fg="White",text="Add Current Semester",font='Helvetica 12 bold').grid(row=0,column=2, pady=10)
tk.Button(frame5,bg="Gray",fg="White",text="Add Previous Semester",font='Helvetica 12 bold').grid(row=1, column=2, pady=5)
tk.Button(frame5,bg="Gray",fg="White",text="Adjust Current Semester",font='Helvetica 12 bold').grid(row=2,column=2, pady=10)
tk.Button(frame5,bg="Gray",fg="White",text="Cummulative Rundown",font='Helvetica 12 bold').grid(row=3,column=2,pady=10)
tk.Button(frame5,bg="Gray",fg="White",text="Potential GPA Calc",font='Helvetica 12 bold').grid(row=4,column=2)

window.mainloop()
