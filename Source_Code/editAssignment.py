'''
Title: Edit Assignment
Window: Edit Assignment System
Author: Ethan Morton
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Edits an assignment in a class
Other Requirements: TKInter for Interface Design.
'''
def EDIT_ASSIGNMENT(course):
    import tkinter as tk
    import os
    import pathlib
    import csv

    # gets the directory of the current/most recent semester
    os.chdir(pathlib.Path(__file__).parent.resolve())
    accountFile = ""
    with open("currentLogin.csv", "r", newline = "") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            accountFile = line[0]
    os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", accountFile, "Semesters"))
    semesters = os.listdir(os.getcwd())
    mostRecentSemesterFile = ""
    mostRecentYear = 0
    mostRecentSession = 0
    for semester in semesters:
        if os.path.isdir(os.path.join(os.getcwd(), semester)):
            year = int(semester[semester.index("_")+1:semester.rindex("_")])
            session = 0
            match semester[semester.rindex("_")+1:].lower():
                case "fall":
                    session = 1
                case "autumn":
                    session = 1
                case "winter":
                    session = 2
                case "spring":
                    session = 3
                case "summer":
                    session = 4
            if (year > mostRecentYear):
                mostRecentYear = year
                mostRecentSemesterFile = semester
            elif (year == mostRecentYear):
                if (session > mostRecentSession):
                    mostRecentSession = session
                    mostRecentSemesterFile = semester
    os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", accountFile, "Semesters", mostRecentSemesterFile))

    window=tk.Tk()
    window.title('Edit Assignment')
    window.geometry("300x250")
    window.configure(bg='grey')

    def Search():
        searchName = nameEntry.get()
        '''
        #search through csv file for matching name
        if found:
            name
            grade
            weight
            assignmentLabel.configure(text = f"Assignment Title: {name}, Assignment Grade: {grade}, Assignment Weight: {weight}")
        '''
        pass

    def Save(course):
        # save assignment info in csv file
        window.destroy()
        import classManager
        classManager.CLASS_MANAGER(course)

    def Back(course):
        window.destroy()
        import classManager
        classManager.CLASS_MANAGER(course)

    nameLabel = tk.Label(window, text="Assignment Title:", bg='grey', fg='white', font=("Helvetica 12 bold"))
    nameLabel.grid(row = 0, column = 0)
    nameEntry = tk.Entry(window)
    nameEntry.grid(row = 0, column = 1)

    searchButton = tk.Button(window, text="Search", bg='grey', fg='white',font=("Helvetica 10 bold"), command = Search)
    searchButton.grid(row = 0, column = 2)

    assignmentLabel = tk.Label(window, text="Assignment Found:", bg='grey', fg='white', font=("Helvetica 12 bold"))
    assignmentLabel.grid(row = 1, column = 0)

    newNameLabel = tk.Label(window, text="Assignment Title:", bg='grey', fg='white', font=("Helvetica 12 bold"))
    newNameLabel.grid(row = 2, column = 0)
    newNameEntry = tk.Entry(window)
    newNameEntry.grid(row = 2, column = 1)

    newGradeLabel = tk.Label(window, text="Assignment Grade:", bg='grey', fg='white', font=("Helvetica 12 bold"))
    newGradeLabel.grid(row = 3, column = 0)
    newGradeEntry = tk.Entry(window)
    newGradeEntry.grid(row = 3, column = 1)

    newWeightLabel = tk.Label(window, text="Assignment Weight:", bg='grey', fg='white', font=("Helvetica 12 bold"))
    newWeightLabel.grid(row = 4, column = 0)
    newWeightEntry = tk.Entry(window)
    newWeightEntry.grid(row = 4, column = 1)

    saveButton = tk.Button(window, text="Save", bg='grey', fg='white',font=("Helvetica 10 bold"), command = lambda: Save(course))
    saveButton.grid(row = 5, column = 0)

    backButton = tk.Button(window, text="Back", bg='grey', fg='white',font=("Helvetica 10 bold"), command = lambda: Back(course))
    backButton.grid(row = 5, column = 0)

    window.mainloop()