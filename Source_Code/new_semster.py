'''
Title: Student Learning Management System
Window: Semester Settings Window
Author: Christian Sarmiento
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Allows student to add a new semester to add classes to
Widgets:
    new_semester - main window
    newSemesterFrame - frame for input and button
    createSemesterLabel - Label for frame
    newYearLabel - Label for year input window
    entryNewYear - year input window
    newSessionLabel - Label for session input window
    entrySessionYear - session input window
    btnNewSemester - Button to create new semester with input   
Other Requirements: TKInter for Interface Design.
'''

# Import Libraries
import tkinter as tk

# Window
new_semester = tk.Tk()
new_semester.title('New Semester') # title
new_semester.geometry('250x150')  # window dimensions
new_semester.configure(bg = 'white')  # color

# Frames
newSemesterFrame = tk.Frame(new_semester,
                            bg = 'lightgrey',
                            width = 100,
                            height = 50)
newSemesterFrame.grid(row = 1, column = 0)

# Label for Creating a New Semester
createSemesterLabel = tk.Label(new_semester,
                               text = 'Create New Semester:',
                               bg = 'lightgrey',
                               fg = 'black',
                               padx = 20,
                               pady = 10)
createSemesterLabel.grid(row = 0, column = 0)

# Label for Inputting New Semester Year
newYearLabel = tk.Label(newSemesterFrame,
                        text = 'Year',
                        bg = 'lightgrey',
                        fg = 'black')
newYearLabel.grid(row = 0, column = 0)

# Entry Window for Year
entryNewYear = tk.Entry(newSemesterFrame,
                        bg = 'white')
entryNewYear.grid(row = 0, column = 1)

# Label for Inputting New Semester Session
newSessionLabel = tk.Label(newSemesterFrame,
                        text = 'Session',
                        bg = 'lightgrey',
                        fg = 'black')
newSessionLabel.grid(row = 1, column = 0)

# Entry Window for Session
entrySessionYear = tk.Entry(newSemesterFrame,
                            bg = 'white')
entrySessionYear.grid(row = 1, column = 1)

# Button to Create New Semester
btnNewSemester = tk.Button(newSemesterFrame,
                           text = 'Create',
                           bg = 'lightgrey',
                           padx = 55)
btnNewSemester.grid(row = 2, column = 1)

new_semester.mainloop()
