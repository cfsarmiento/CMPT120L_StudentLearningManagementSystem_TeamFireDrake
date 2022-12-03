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
    import os
    import csv
    import pathlib
    import sourceCodeLibrary
    dict = sourceCodeLibrary.GetAccountDirectory()
    os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", dict["accountPath"], "Semesters"))

    # Window
    new_semester = tk.Tk()
    new_semester.title('Add Current Semester') # title
    new_semester.geometry('400x300')  # window dimensions
    new_semester.configure(bg = 'grey')  # color

    def CreateSemester():
        year = entryNewYear.get() # year must be an integer
        session = entrySessionYear.get() # session must either be "fall", "winter", "spring", "summer"  -  not case sensative
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
        except:
            createSemesterLabel.configure(text = "The Year must be an integer")
            return
        else:
            if season != 0:
                if not os.path.exists(f"Semester_{year}_{session}"):
                    os.makedirs(f"Semester_{year}_{session}")
                os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", dict["accountPath"], "Semesters", f"Semester_{year}_{session}"))
                with open("semesterInfo.csv", "w", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["Year: " + year, "Session: " + session, "GPA: 0", "Total Course Credits: 0"])
                new_semester.destroy()
                import mainPage
                mainPage.MAIN_PAGE()
            else:
                createSemesterLabel.configure(text = "The session must be entered as\nFall or Autumn\nWinter\nSpring\nSummer")

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

    createSemesterLabel = tk.Label(newSemesterFrame, text = "", bg = 'grey', fg = 'white', font = 'Helvetica 12 bold', padx = 20, pady = 10)
    createSemesterLabel.grid(row = 3, column = 1)

    # Button to Create New Semester
    btnNewSemester = tk.Button(newSemesterFrame,
                            text = 'Create',
                            bg = 'grey', fg='white', font='Helvetica 12 bold',
                            padx = 55,
                            command = CreateSemester)
    btnNewSemester.grid(row = 2, column = 1)

    backButton = tk.Button(newSemesterFrame,text = 'Back',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = Back)
    backButton.grid(row = 4, column = 1)

    new_semester.mainloop()