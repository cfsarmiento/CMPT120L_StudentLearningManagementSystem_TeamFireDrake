#Title: Student Learning Management System
#Window: Class Management System
#Authors: Cody Carruthers and Gabrielle Knapp
#Class: CMPT120L
#Professor: Reza Sadeghi
#Goal: Prints the classes, homework, weights, grades for the student
#Other Requirements: TKInter for Interface Design.
from tkinter import *
def CLASS_MANAGER(course):
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

    # get info from the course
    info = ["Course: ","Credits: ","Homework: ","Test: ","Project: ","Quiz: ","Essay: "]
    with open("course" + course + ".csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            for i, row in enumerate(line):
                if "Course: " in row:
                    info[i] = row
                elif "Credits: " in row:
                    info[i] = row
                elif "Homework: " in row:
                    info[i] = row
                elif "Test: " in row:
                    info[i] = row
                elif "Project: " in row:
                    info[i] = row
                elif "Quiz: " in row:
                    info[i] = row
                elif "Essay: " in row:
                    info[i] = row
    # info should look something like this as an example
    # ["Course: CMPT_120","Credits: 4","Homework: 20","Test: 40","Project: 40","Quiz: ","Essay: "]

    window=Tk()
    window.title('Class Manager')
    window.geometry('1000x300')
    window.configure(bg='grey')

    leftFrame = tk.Frame(window).grid(column=0, row=0)
    rightFrame = tk.Frame(window).grid(column=1, row=0)

    def Back():
        window.destroy()
        import mainPage
        mainPage.MAIN_PAGE()
    
    def AddAssignment(course):
        window.destroy()
        import addAssignment
        addAssignment.ADD_ASSIGNMENT(course)

    def EditAssignment(course):
        window.destroy()
        import editAssignment
        editAssignment.EDIT_ASSIGNMENT(course)

    def RemoveAssignment(course):
        window.destroy()
        import removeAssignment
        removeAssignment.REMOVE_ASSIGNMENT(course)

    backButton = tk.Button(rightFrame,text = 'Back',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = Back)
    backButton.grid(row = 0, column = 0)

    addAssignment = tk.Button(rightFrame,text = 'Add Assignment',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = lambda: AddAssignment(course))
    addAssignment.grid(row = 1, column = 0)

    editAssignment = tk.Button(rightFrame,text = 'Edit Assignment',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = lambda: EditAssignment(course))
    editAssignment.grid(row = 2, column = 0)

    removeAssignment = tk.Button(rightFrame,text = 'Remove Assignment',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = lambda: RemoveAssignment(course))
    removeAssignment.grid(row = 3, column = 0)

    assignments = []
    with open("course"+course+".csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for i, line in enumerate(reader):
            if (i == 0):
                continue
            assignments.append(line)

    headerTitleCanvas = Canvas(leftFrame, width= 170, height= 50, bg="grey")
    headerTitleCanvas.create_text(80,25, text="Assignment Type", fill="white", font=('Helvetica 12 bold'))
    headerTitleCanvas.grid(row=0,column=0)

    headerGradeCanvas = Canvas(leftFrame, width= 70, height= 50, bg="grey")
    headerGradeCanvas.create_text(25,25, text="Grade", fill="white", font=('Helvetica 12 bold'))
    headerGradeCanvas.grid(row=0,column=1)

    headerWeightCanvas = Canvas(leftFrame, width= 120, height= 50, bg="grey")
    headerWeightCanvas.create_text(30,25, text="Weight", fill="white", font=('Helvetica 12 bold'))
    headerWeightCanvas.grid(row=0,column=2)

    canvases = []
    for rowIndex, assignment in enumerate(assignments):
        for columnIndex in range(0,2):
            canvas = None
            match columnIndex:
                case 0:
                    canvas = Canvas(leftFrame, width= 170, height= 50, bg="grey")
                    canvas.create_text(85,25, text=assignment[columnIndex], fill="white", font=('Helvetica 12 bold'))
                    canvas.grid(row=rowIndex+1,column=columnIndex)
                case 1:
                    canvas = Canvas(leftFrame, width= 70, height= 50, bg="grey")
                    canvas.create_text(35,25, text=assignment[columnIndex], fill="white", font=('Helvetica 12 bold'))
                    canvas.grid(row=rowIndex+1,column=columnIndex)
                case 2:
                    canvas = Canvas(leftFrame, width= 85, height= 50, bg="grey")
                    canvas.create_text(40,25, text=assignment[columnIndex], fill="white", font=('Helvetica 12 bold'))
                    canvas.grid(row=rowIndex+1,column=columnIndex)
            canvases.append(canvas)

    window.mainloop()