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
    import os
    import csv
    import pathlib
    import sourceCodeLibrary
    dict = sourceCodeLibrary.GetAccountDirectory()
    os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", dict["accountPath"], "Semesters"))

    # Window
    semester_settings = tk.Tk()
    semester_settings.title('Add Previous Semester')  # title for window
    semester_settings.geometry('450x300')  # window size
    semester_settings.configure(bg ='grey')  # color

    def Finalize():
        year = entryYear.get() # year must be an integer
        session = entrySession.get() # session must either be "fall", "winter", "spring", "summer"  -  not case sensative
        gpa = entryFinalGPA.get() # gpa must be a float
        totalCredits = totalCreditsEntry.get()
        season = 0
        match session.lower():
            case "fall":
                season = 1
            case "autumn":  # just in case anyone writes this
                season = 1
            case "winter":
                season = 2
            case "spring":
                season = 3
            case "summer":
                season = 4
        try:
            int(year)
            float(gpa)
            int(totalCredits)
        except:
            createSemesterLabel.configure(text="Year and Total Credits must be an integer,\nand GPA must be a decimal or integer")
        else:
            if season != 0:
                if not os.path.exists(f"Semester_{year}_{session}"):
                    os.makedirs(f"Semester_{year}_{session}")
                os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", dict["accountPath"], "Semesters", f"Semester_{year}_{session}"))
                with open("semesterInfo.csv", "w", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["Year: " + year, "Session: " + session, "GPA: " + gpa, "Total Course Credits: " + totalCredits])
                import sourceCodeLibrary
                sourceCodeLibrary.CalculateCumulativeGPA()
                semester_settings.destroy()
                import mainPage
                mainPage.MAIN_PAGE()
            else:
                createSemesterLabel.configure(text="The session must be entered as\nFall or Autumn\nWinter\nSpring\nSummer")

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

    totalCreditsLabel = tk.Label(inputFrame,text = 'Total Course Credits:',bg = 'grey',fg = 'white')
    totalCreditsLabel.grid(row = 3, column = 0)
    totalCreditsEntry = tk.Entry(inputFrame,bg = 'white')
    totalCreditsEntry.grid(row = 3, column = 1)

    createSemesterLabel = tk.Label(inputFrame, text = "", bg = 'grey', fg = 'white', font = 'Helvetica 12 bold', padx = 20, pady = 10)
    createSemesterLabel.grid(row = 4, column = 1)

    # Button to Finalize Past GPA Entry
    btnFinalize = tk.Button(inputFrame,
                            text = 'Finalize',
                            bg = 'grey',
                            fg = 'white',
                            padx = 55,
                            command = Finalize)
    btnFinalize.grid(row = 5, column = 1)

    backButton = tk.Button(inputFrame,text = 'Back',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = Back)
    backButton.grid(row = 6, column = 1)
                                
    semester_settings.mainloop()