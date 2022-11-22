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
    import csv
    import sourceCodeLibrary
    mostRecentSemesterDirectory = sourceCodeLibrary.GetMostRecentSemesterDirectory()
    os.chdir(mostRecentSemesterDirectory)

    # get info from the course
    info = ["Course: ", "Credits: ", "Grade: ", "Homework: ", "Test: ", "Project: ", "Quiz: ", "Essay: "]
    with open("course"+course+".csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            for i, row in enumerate(line):
                if "Course: " in row or " Credits: " in row or "Grade: " in row or " Homework: " in row or " Test: " in row or " Project: " in row or " Quiz: " in row or " Essay: " in row:
                    info[i] = row
    # info should look something like this as an example
    # ["Course: CMPT_120","Credits: 4", "Grade: 94", "Homework: 20","Test: 40","Project: 40","Quiz: ","Essay: "]

    window=Tk()
    window.title('Class Manager')
    window.geometry('1000x300')
    window.configure(bg='grey')

   # leftFrame = tk.Frame(window,width=500,height=500, bg="orange").grid(column=0, row=0)
    #rightFrame = tk.Frame(window,width=500,height=500, bg="blue").grid(column=1, row=0)

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

    infoText = ""
    for s in info:
        infoText+=s
    courseInfoLabel = tk.Label(window, bg="grey", fg="white", text=infoText, font='Helvetica 12 bold').grid(row=0,column=0)

    backButton = tk.Button(window,text = 'Back',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = Back)
    backButton.grid(row = 1, column = 0)

    addAssignment = tk.Button(window,text = 'Add Assignment',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = lambda: AddAssignment(course))
    addAssignment.grid(row = 2, column = 0)

    editAssignment = tk.Button(window,text = 'Edit Assignment',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = lambda: EditAssignment(course))
    editAssignment.grid(row = 3, column = 0)

    removeAssignment = tk.Button(window,text = 'Remove Assignment',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = lambda: RemoveAssignment(course))
    removeAssignment.grid(row = 4, column = 0)

    assignments = []
    with open("course"+course+".csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for i, line in enumerate(reader):
            if (i == 0):
                continue
            assignments.append(line)

    headerGradeLabel = Canvas(window, width= 70, height= 50, bg="grey")
    headerGradeLabel.create_text(25,25, text="Grade", fill="white", font=('Helvetica 12 bold'))
    headerGradeLabel.grid(row=1,column=3)

    headerWeightLabel = Canvas(window, width= 120, height= 50, bg="grey")
    headerWeightLabel.create_text(30,25, text="Weight", fill="white", font=('Helvetica 12 bold'))
    headerWeightLabel.grid(row=1,column=4)

    headerWeightLabel = Canvas(window, width= 170, height= 50, bg="grey")
    headerWeightLabel.create_text(80,25, text="Assignment Title", fill="white", font=('Helvetica 12 bold'))
    headerWeightLabel.grid(row=1,column=2)

    for rowIndex, assignment in enumerate(assignments):
        for columnIndex in range(0,3):
            match columnIndex:
                case 0:
                    canvas = Canvas(window, width= 170, height= 50, bg="grey")
                    canvas.create_text(85,25, text=assignment[columnIndex], fill="white", font=('Helvetica 12 bold'))
                    canvas.grid(row=rowIndex+2,column=columnIndex+2)
                case 1:
                    canvas = Canvas(window, width= 70, height= 50, bg="grey")
                    canvas.create_text(35,25, text=assignment[columnIndex], fill="white", font=('Helvetica 12 bold'))
                    canvas.grid(row=rowIndex+2,column=columnIndex+2)
                case 2:
                    canvas = Canvas(window, width= 85, height= 50, bg="grey")
                    canvas.create_text(40,25, text=assignment[columnIndex], fill="white", font=('Helvetica 12 bold'))
                    canvas.grid(row=rowIndex+2,column=columnIndex+2)

    window.mainloop()