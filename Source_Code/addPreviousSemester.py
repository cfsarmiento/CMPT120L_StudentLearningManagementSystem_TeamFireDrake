'''
Title: Student Learning Management System
Window: Add Previous Semester
Author: Christian Sarmiento
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Allows student to add past GPAs 
Widgets:
    semester_settings - main window
    inputFrame - frame for all the user input
    addGPALabel - Label for inputFrame to input gpa info
    yearLabel - Label to go next to input spot for year
    entryYear - Text box so user can put the year for past gpa
    sessionLabel - Label for session (Fall/Winter/Spring/Summer)
    entrySession - Text box so user can input the session
    finalGPALabel - Label for GPA entry box
    entryFinalGPA - Text box so user can input final gpa
    btnFinalize - Button to finalize GPA into system (cannot be undone)
Other Requirements: TKInter for Interface Design.
'''
def ADD_PREVIOUS_SEMESTER():
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
    semester_settings = tk.Tk()
    semester_settings.title('Add Previous Semester')  # title for window
    semester_settings.geometry('300x175')  # window size
    semester_settings.configure(bg ='grey')  # color

    def Finalize():
        year = entryYear.get() # year must be an integer
        session = entrySession.get() # session must either be "fall", "winter", "spring", "summer"  -  not case sensative
        gpa = entryFinalGPA.get() # gpa must be a float
        if not os.path.exists(f"Semester_{year}_{session}"):
            os.makedirs(f"Semester_{year}_{session}")
        os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", accountFile, "Semesters", f"Semester_{year}_{session}"))
        with open("semesterInfo.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Year: " + year, "Session: " + session, "GPA: " + gpa])
        semester_settings.destroy()
        import mainPage
        mainPage.MAIN_PAGE()

    def Back():
        semester_settings.destroy()
        import mainPage
        mainPage.MAIN_PAGE()

    # Frames
    inputFrame = tk.Frame(semester_settings,
                        bg = 'grey',
                        width = 300,
                        height= 100)
    newSemesterFrame = tk.Frame(semester_settings,
                                bg = 'grey',
                                width = 200,
                                height = 50)

    inputFrame.grid(row = 1, column = 0)
    newSemesterFrame.grid(row = 4, column = 0)

    # Label for Add Past Final Semester GPA
    addGPALabel = tk.Label(semester_settings,
                        text = 'Add a Past Final Semester GPA:',
                        bg = 'grey',
                        fg = 'white',
                        padx = 10,
                        pady = 10)
    addGPALabel.grid(row = 0, column = 0)

    # Label for Year Entry
    yearLabel = tk.Label(inputFrame,
                        text = 'Year:',
                        bg = 'grey',
                        fg = 'white')
    yearLabel.grid(row = 0, column = 0)

    # Entry Window for Year
    entryYear = tk.Entry(inputFrame,
                        bg = 'white')
    entryYear.grid(row = 0, column = 1)

    # Label for Session Entry
    sessionLabel = tk.Label(inputFrame,
                        text = 'Session:',
                        bg = 'grey',
                        fg = 'white')
    sessionLabel.grid(row = 1, column = 0)

    # Entry Window for Session
    entrySession = tk.Entry(inputFrame,
                        bg = 'white')
    entrySession.grid(row = 1, column = 1)

    # Label for Final GPA Entry
    finalGPALabel = tk.Label(inputFrame,
                        text = 'Final GPA:',
                        bg = 'grey',
                        fg = 'white')
    finalGPALabel.grid(row = 2, column = 0)

    # Entry Window for Final GPA
    entryFinalGPA = tk.Entry(inputFrame,
                        bg = 'white')
    entryFinalGPA.grid(row = 2, column = 1)

    # Button to Finalize Past GPA Entry
    btnFinalize = tk.Button(inputFrame,
                            text = 'Finalize',
                            bg = 'grey',
                            fg = 'white',
                            padx = 55,
                            command = Finalize)
    btnFinalize.grid(row = 3, column = 1)

    backButton = tk.Button(inputFrame,text = 'Back',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = Back)
    backButton.grid(row = 4, column = 1)
                                
    semester_settings.mainloop()
