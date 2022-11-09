'''
Title: Student Learning Management System
Window: Finalize Semester Window
Author: Ethan Morton
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Saves the information that was entered into the current semester.
Widgets: Cancel button, save button, text
Other Requirements: TKInter for Interface Design.
'''
import tkinter as tk
window = tk.Tk()
window.title('Finalize Semester')
window.geometry('351x67')
window.configure(bg = "black")

descriptionText0 = tk.Label(window, text = "Save the information in this semester?", bg = "black", fg = 'white')
descriptionText0.grid(column = 1, row = 0)

descriptionText1 = tk.Label(window, text = "This is permanent and you cannot go back to edit.", bg = "black", fg = 'red')
descriptionText1.grid(column = 1, row = 1)

cancelButton = tk.Button(window, bg = "red", fg = "white", text = "Cancel")
cancelButton.grid(column = 0, row = 2)

saveButton = tk.Button(window, bg = "green", fg = "white", text = "Save")
saveButton.grid(column = 2, row = 2)

window.mainloop()