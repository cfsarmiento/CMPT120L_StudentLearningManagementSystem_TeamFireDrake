'''
Title: Student Learning Management System
Window: Settings Window
Author: Ethan Morton
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Presents the user with a menu to add or edit class information and go to semester settings
Widgets: Add class button, edit class button, semester settings button, text
Other Requirements: TKInter for Interface Design.
'''
import tkinter as tk
window = tk.Tk()
window.title('Settings')
window.geometry('225x77')
window.configure(bg = "black")

addClassButton = tk.Button(window, bg = "red", fg = "white", text = "Add Class")
addClassButton.grid(column = 0, row = 0)

removeClassButton = tk.Button(window, bg = "red", fg = "white", text = "Remove Class")
removeClassButton.grid(column = 0, row = 1)

semesterSettingsButton = tk.Button(window, bg = "yellow", fg = "black", text = "Semester Settings")
semesterSettingsButton.grid(column = 0, row = 2)

window.mainloop()