'''
Title: Add Assignment
Window: Add Assignment System
Author: Ethan Morton
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Adds an assignment to a class
Other Requirements: TKInter for Interface Design.
'''
def ADD_ASSIGNMENT(course):
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
    window.title('Add Assignment')
    window.geometry("300x250")
    window.configure(bg='grey')

    def Add():
        try:
            name = nameEntry.get()
            grade = gradeEntry.get()
            weight = weightEntry.get()
            with open("course"+course+".csv", "a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([name, grade, weight])
            addLabel.configure(text = "Assignment added: " + name)
            # it also needs to update the gpa
            # UpdateGrades()
        except:
            addLabel.configure(text = "Could not add assignment: " + name)
    
    def Back(course):
        window.destroy()
        import classManager
        classManager.CLASS_MANAGER(course)

    nameLabel = tk.Label(window, text="Assignment Title:", bg='grey', fg='white', font=("Helvetica 12 bold"))
    nameLabel.grid(row = 0, column = 0)
    nameEntry = tk.Entry(window)
    nameEntry.grid(row = 0, column = 1)

    gradeLabel = tk.Label(window, text="Assignment Grade:", bg='grey', fg='white', font=("Helvetica 12 bold"))
    gradeLabel.grid(row = 1, column = 0)
    gradeEntry = tk.Entry(window)
    gradeEntry.grid(row = 1, column = 1)

    weightLabel = tk.Label(window, text="Assignment Weight:", bg='grey', fg='white', font=("Helvetica 12 bold"))
    weightLabel.grid(row = 2, column = 0)
    weightEntry = tk.Entry(window)
    weightEntry.grid(row = 2, column = 1)

    addButton = tk.Button(window, text="Add", bg='grey', fg='white',font=("Helvetica 10 bold"), command = Add)
    addButton.grid(row = 3, column = 0)

    addLabel = tk.Label(window, text="", bg='grey', fg='white', font=("Helvetica 12 bold"))
    addLabel.grid(row = 4, column = 0)

    backButton = tk.Button(window, text="Back", bg='grey', fg='white',font=("Helvetica 10 bold"), command = lambda: Back(course))
    backButton.grid(row = 5, column = 0)

    window.mainloop()