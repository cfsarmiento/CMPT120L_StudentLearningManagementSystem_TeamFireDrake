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
    import csv
    import sourceCodeLibrary
    mostRecentSemesterDirectory = sourceCodeLibrary.GetMostRecentSemesterDirectory()
    os.chdir(mostRecentSemesterDirectory)

    window=tk.Tk()
    window.title('Edit Assignment')
    window.geometry("400x250")
    window.configure(bg='grey')

    def Search():
        searchName = nameEntry.get()
        assignmentLabel.configure(text = "Could not find assignment: " + searchName)
        with open("course"+course+".csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                if (searchName == line[0]):
                    assignmentLabel.configure(text = "Assignment Found: " + line[0])
                    break

    def Save():
        searchName = nameEntry.get()
        newName = newNameEntry.get()
        newGrade = newGradeEntry.get()
        newWeight = newWeightEntry.get()
        found = False
        courseFile = []
        with open("course"+course+".csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                if (line[0] == searchName):
                    courseFile.append([newName, newGrade, newWeight])
                    found = True
                else:
                    courseFile.append(line)
        if not found:
            assignmentLabel.configure(text = "Could not save assignment: " + newName)
            return
        with open("course"+course+".csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(courseFile)
        assignmentLabel.configure(text = "Assignment saved: " + newName)
        import sourceCodeLibrary
        sourceCodeLibrary.CalculateCourseGrade(course)

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

    assignmentLabel = tk.Label(window, text="", bg='grey', fg='white', font=("Helvetica 12 bold"))
    assignmentLabel.grid(row = 1, column = 0)

    newNameLabel = tk.Label(window, text="New Assignment Title:", bg='grey', fg='white', font=("Helvetica 12 bold"))
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

    saveButton = tk.Button(window, text="Save", bg='grey', fg='white',font=("Helvetica 10 bold"), command = Save)
    saveButton.grid(row = 5, column = 0)

    backButton = tk.Button(window, text="Back", bg='grey', fg='white',font=("Helvetica 10 bold"), command = lambda: Back(course))
    backButton.grid(row = 6, column = 0)

    window.mainloop()