'''
Title: Remove Assignment
Window: Remove Assignment System
Author: Ethan Morton
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Removes an assignment from a class
Other Requirements: TKInter for Interface Design.
'''
def REMOVE_ASSIGNMENT(course):
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
    window.title('Remove Assignment')
    window.geometry("400x250")
    window.configure(bg='grey')

    def Search():
        try:
            searchName = nameEntry.get()
            with open("course"+course+".csv", "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
            assignmentLabel.configure(text = "Assignment Found: " + searchName)
        except:
            assignmentLabel.configure(text = "Could not find assignment: " + searchName)

    def Remove():
        try:
            searchName = nameEntry.get()
            courseFile = []
            with open("course"+course+".csv", "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                for line in reader:
                    if (line[0] != searchName):
                        courseFile.append(line)
            with open("course"+course+".csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(courseFile)
            assignmentLabel.configure(text = "Assignment removed: " + searchName)
            # it also needs to update the gdp
        except:
            assignmentLabel.configure(text = "Could not remove assignment: " + searchName)

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

    removeButton = tk.Button(window, text="Remove", bg='grey', fg='white',font=("Helvetica 10 bold"), command = Remove)
    removeButton.grid(row = 5, column = 0)

    backButton = tk.Button(window, text="Back", bg='grey', fg='white',font=("Helvetica 10 bold"), command = lambda: Back(course))
    backButton.grid(row = 6, column = 0)

    window.mainloop()