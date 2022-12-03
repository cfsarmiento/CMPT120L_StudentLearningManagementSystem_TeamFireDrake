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
    import csv
    import sourceCodeLibrary
    mostRecentSemesterDirectory = sourceCodeLibrary.GetMostRecentSemesterDirectory()
    os.chdir(mostRecentSemesterDirectory)

    window=tk.Tk()
    window.title('Remove Assignment')
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

    def Remove():
        searchName = nameEntry.get()
        courseFile = []
        found = False
        with open("course"+course+".csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                if (line[0] != searchName):
                    courseFile.append(line)
                else:
                    found = True
        if not found:
            assignmentLabel.configure(text = "Could not remove assignment: " + searchName)
            return
        with open("course"+course+".csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(courseFile)
        assignmentLabel.configure(text = "Assignment removed: " + searchName)
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

    removeButton = tk.Button(window, text="Remove", bg='grey', fg='white',font=("Helvetica 10 bold"), command = Remove)
    removeButton.grid(row = 5, column = 0)

    backButton = tk.Button(window, text="Back", bg='grey', fg='white',font=("Helvetica 10 bold"), command = lambda: Back(course))
    backButton.grid(row = 6, column = 0)

    window.mainloop()