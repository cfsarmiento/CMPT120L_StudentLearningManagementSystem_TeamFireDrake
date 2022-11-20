'''
Title: Adjust Current Semester
Window: Adjust Current Semester Window
Author: Gabrielle Knapp
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Allow users to add class, remove class, or edit class
Widgets: labels, textfields, and buttons
Other Requirements: TKInter for Interface Design.
'''
import tkinter as tk

# Window
window = tk.Tk()
window.title('Adjust Current Semester')  # title for window
window.geometry('300x300')  # length x width
window.configure(bg = 'grey')  # background color

#Frame
frame1 = tk.Frame(window, bg = 'grey', width = 200).grid(row=1, column=1)

#Label
lbl1=tk.Label(frame1, text="Select an option: ", bg = 'grey',fg = 'white',font = 'Helvetica 12 bold').grid(row = 0, column = 1)

#Buttons
btn1=tk.Button(frame1,text = "Add Class",bg = 'grey',fg = 'white',font = 'Helvetica 12 bold').grid(row = 1, column = 1)
btn2=tk.Button(frame1,text = "Remove Class",bg = 'grey',fg = 'white',font = 'Helvetica 12 bold').grid(row = 2, column = 1)
btn3=tk.Button(frame1,text = "Add/Edit Class Grade",bg = 'grey',fg = 'white',font = 'Helvetica 12 bold').grid(row = 3, column = 1)
