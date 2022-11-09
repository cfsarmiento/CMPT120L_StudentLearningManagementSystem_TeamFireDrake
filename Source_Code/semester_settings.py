'''
Title: Student Learning Management System
Window: Semester Settings Window
Author: Christian Sarmiento
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Allows student to add past GPAs (if applicable) and as well as being
      able to make a new semster to keep classes in. Displays current semester
Widgets:
    semester_settings - main window
    inputFrame - frame for all the user input
    newSemesterFrame - frame for new semster button and current semster
    addGPALabel - Label for inputFrame to input gpa info
    newSemesterLabel - Label for newSemesterFrame
    yearLabel - Label to go next to input spot for year
    entryYear - Text box so user can put the year for past gpa
    sessionLabel - Label for session (Fall/Winter/Spring/Summer)
    entrySession - Text box so user can input the session
    finalGPALabel - Label for GPA entry box
    entryFinalGPA - Text box so user can input final gpa
    btnFinalize - Button to finalize GPA into system (cannot be undone)
    btnNewSemester - Button that opens up new page for creating a new semster
    currentSemesterLabel - Label to show current semester
    txtCurrentSemester - Text box so that backend can output current semster here
    
Other Requirements: TKInter for Interface Design.
'''

# Import Libraries
import tkinter as tk

# Window
semester_settings = tk.Tk()
semester_settings.title('Semester Settings')  # title for window
semester_settings.geometry('400x250')  # window size
semester_settings.configure(bg ='white')  # color

# Frames
inputFrame = tk.Frame(semester_settings,
                      bg = 'lightgrey',
                      width = 300,
                      height= 100)
newSemesterFrame = tk.Frame(semester_settings,
                            bg = 'lightgrey',
                            width = 200,
                            height = 50)

inputFrame.grid(row = 1, column = 0)
newSemesterFrame.grid(row = 4, column = 0)

# Label for Add Past Final Semester GPA
addGPALabel = tk.Label(semester_settings,
                       text = 'Add a Past Final Semester GPA:',
                       bg = 'lightgrey',
                       fg = 'black',
                       padx = 10,
                       pady = 10)
addGPALabel.grid(row = 0, column = 0)

# Label for Add New Semester
newSemesterLabel = tk.Label(semester_settings,
                            text = 'Add a New Semester',
                            bg = 'lightgrey',
                            fg = 'black',
                            padx = 10,
                            pady = 10)
newSemesterLabel.grid(row = 3, column = 0)

# Label for Year Entry
yearLabel = tk.Label(inputFrame,
                     text = 'Year',
                     bg = 'lightgrey',
                     fg = 'black')
yearLabel.grid(row = 0, column = 0)

# Entry Window for Year
entryYear = tk.Entry(inputFrame,
                     bg = 'white')
entryYear.grid(row = 0, column = 1)

# Label for Session Entry
sessionLabel = tk.Label(inputFrame,
                     text = 'Session',
                     bg = 'lightgrey',
                     fg = 'black')
sessionLabel.grid(row = 1, column = 0)

# Entry Window for Session
entrySession = tk.Entry(inputFrame,
                     bg = 'white')
entrySession.grid(row = 1, column = 1)

# Label for Final GPA Entry
finalGPALabel = tk.Label(inputFrame,
                     text = 'Final GPA',
                     bg = 'lightgrey',
                     fg = 'black')
finalGPALabel.grid(row = 2, column = 0)

# Entry Window for Final GPA
entryFinalGPA = tk.Entry(inputFrame,
                     bg = 'white')
entryFinalGPA.grid(row = 2, column = 1)

# Button to Finalize Past GPA Entry
btnFinalize = tk.Button(inputFrame,
                        text = 'Finalize',
                        bg = 'red',
                        fg = 'black',
                        padx = 55)
btnFinalize.grid(row = 3, column = 1)

# Button to Add a New Semester
btnNewSemester = tk.Button(newSemesterFrame,
                           text = 'New Semester',
                           bg = 'red',
                           fg = 'black',
                           pady = 10,
                           padx = 20)
btnNewSemester.grid(row = 0, column = 0)

# Label to Display Current Semester
currentSemesterLabel = tk.Label(newSemesterFrame,
                                text = 'Current Semester:',
                                bg = 'lightgrey',
                                fg = 'black',
                                padx = 10)
currentSemesterLabel.grid(row = 0, column = 1)

# Text Window to Display Current Semester
txtCurrentSemester = tk.Text(newSemesterFrame,
                             bg = 'white',
                             width = 10,
                             height = 2)
txtCurrentSemester.grid(row = 0, column = 2)
                             
semester_settings.mainloop()



