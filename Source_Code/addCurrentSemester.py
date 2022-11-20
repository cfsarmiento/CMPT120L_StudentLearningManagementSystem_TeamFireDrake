'''
Title: Student Learning Management System
Window: Add current Semester
Author: Christian Sarmiento
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Allows student to add a new semester which they can add classes to
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
def ADD_CURRENT_SEMESTER():
    import tkinter as tk
    #from tkinter import *
    import os
    import csv
    import pathlib
    os.chdir(pathlib.Path(__file__).parent.resolve())
    accountFile = ""
    with open("currentLogin.csv", "r", newline = "") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            accountFile = line[0]
    os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", accountFile, "Semesters"))

    # Window
    new_semester = tk.Tk()
    new_semester.title('Add Current Semester') # title
    new_semester.geometry('300x175')  # window dimensions
    new_semester.configure(bg = 'grey')  # color

    def CreateSemester():
        year = entryNewYear.get() # year must be an integer
        session = entrySessionYear.get() # session must either be "fall", "winter", "spring", "summer"  -  not case sensative
        if not os.path.exists(f"Semester_{year}_{session}"):
            os.makedirs(f"Semester_{year}_{session}")
        os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", accountFile, "Semesters", f"Semester_{year}_{session}"))
        with open("semesterInfo.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Year: " + year, "Session: " + session, "GPA: "])
        new_semester.destroy()
        import mainPage
        mainPage.MAIN_PAGE()

    def Back():
        new_semester.destroy()
        import mainPage
        mainPage.MAIN_PAGE()

    # Frames
    newSemesterFrame = tk.Frame(new_semester,
                                bg = 'grey',
                                width = 100,
                                height = 50)
    newSemesterFrame.grid(row = 1, column = 0)

    # Label for Creating a New Semester
    createSemesterLabel = tk.Label(new_semester,
                                text = 'Create Current Semester:',
                                bg = 'grey',
                                fg = 'white',
                                font = 'Helvetica 12 bold',
                                padx = 20,
                                pady = 10)
    createSemesterLabel.grid(row = 0, column = 0)

    # Label for Inputting New Semester Year
    newYearLabel = tk.Label(newSemesterFrame,
                            text = 'Year',
                            bg = 'grey',
                            fg = 'white',
                            font='Helvetica 12 bold')
    newYearLabel.grid(row = 0, column = 0)

    # Entry Window for Year
    entryNewYear = tk.Entry(newSemesterFrame,
                            bg = 'grey')
    entryNewYear.grid(row = 0, column = 1)

    # Label for Inputting New Semester Session
    newSessionLabel = tk.Label(newSemesterFrame,
                            text = 'Session',
                            bg = 'grey',
                            fg = 'white',
                            font ='Helvetica 12 bold')
    newSessionLabel.grid(row = 1, column = 0)

    # Entry Window for Session
    entrySessionYear = tk.Entry(newSemesterFrame,
                                bg = 'grey')
    entrySessionYear.grid(row = 1, column = 1)

    # Button to Create New Semester
    btnNewSemester = tk.Button(newSemesterFrame,
                            text = 'Create',
                            bg = 'grey', fg='white', font='Helvetica 12 bold',
                            padx = 55,
                            command = CreateSemester)
    btnNewSemester.grid(row = 2, column = 1)

    backButton = tk.Button(newSemesterFrame,text = 'Back',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = Back)
    backButton.grid(row = 3, column = 1)

    new_semester.mainloop()