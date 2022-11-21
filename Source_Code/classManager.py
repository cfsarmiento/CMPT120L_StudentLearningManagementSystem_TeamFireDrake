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

    #Create a canvas object
    canvas=Canvas(window, width= 170, height= 50, bg="grey")
    canvas2=Canvas(window, width= 70, height= 50, bg="grey")
    canvas3=Canvas(window, width= 120, height= 50, bg="grey")
    canvas4=Canvas(window, width= 85, height= 50, bg="grey")
    canvas5=Canvas(window, width= 170, height= 50, bg="grey")
    canvas6=Canvas(window, width= 170, height= 50, bg="grey")
    canvas7=Canvas(window, width= 170, height= 50, bg="grey")
    canvas8=Canvas(window, width= 170, height= 50, bg="grey")
    canvas9=Canvas(window, width= 70, height= 50, bg="grey")
    canvas10=Canvas(window, width= 70, height= 50, bg="grey")
    canvas11=Canvas(window, width= 70, height= 50, bg="grey")
    canvas12=Canvas(window, width= 70, height= 50, bg="grey")
    canvas13=Canvas(window, width= 120, height= 50, bg="grey")
    canvas14=Canvas(window, width= 120, height= 50, bg="grey")
    canvas15=Canvas(window, width= 120, height= 50, bg="grey")
    canvas16=Canvas(window, width= 120, height= 50, bg="grey")
    canvas17=Canvas(window, width= 85, height= 50, bg="grey")
    canvas18=Canvas(window, width= 85, height= 50, bg="grey")
    canvas19=Canvas(window, width= 85, height= 50, bg="grey")
    canvas20=Canvas(window, width= 85, height= 50, bg="grey")

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

    backButton = tk.Button(window,text = 'Back',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = Back)
    backButton.grid(row = 0, column = 4)

    addAssignment = tk.Button(window,text = 'Add Assignment',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = lambda: AddAssignment(course))
    addAssignment.grid(row = 1, column = 4)

    editAssignment = tk.Button(window,text = 'Edit Assignment',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = lambda: EditAssignment(course))
    editAssignment.grid(row = 2, column = 4)

    removeAssignment = tk.Button(window,text = 'Remove Assignment',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = lambda: RemoveAssignment(course))
    removeAssignment.grid(row = 3, column = 4)

    #Add a text in Canvas
    canvas.create_text(80,25, text="Assignment Type", fill="white", font=('Helvetica 12 bold'))
    canvas.grid(row=0,column=0)

    canvas2.create_text(25,25, text="Grade", fill="white", font=('Helvetica 12 bold'))
    canvas2.grid(row=0, column=1)

    canvas4.create_text(30,25, text="Weight", fill="white", font=('Helvetica 12 bold'))
    canvas4.grid(row=0, column=2)

    canvas5.create_text(85,25, text="Assignment Type #1", fill="white", font=('Helvetica 12 bold'))
    canvas5.grid(row=1, column=0)

    canvas6.create_text(85,25, text="Assignment Type #2", fill="white", font=('Helvetica 12 bold'))
    canvas6.grid(row=2, column=0)

    canvas7.create_text(85,25, text="Assignment Type #3", fill="white", font=('Helvetica 12 bold'))
    canvas7.grid(row=3, column=0)

    canvas8.create_text(85,25, text="Assignment Type #4", fill="white", font=('Helvetica 12 bold'))
    canvas8.grid(row=4, column=0)

    canvas9.create_text(35,25, text="Grade #1", fill="white", font=('Helvetica 12 bold'))
    canvas9.grid(row=1, column=1)

    canvas10.create_text(35,25, text="Grade #2", fill="white", font=('Helvetica 12 bold'))
    canvas10.grid(row=2, column=1)

    canvas11.create_text(35,25, text="Grade #3", fill="white", font=('Helvetica 12 bold'))
    canvas11.grid(row=3, column=1)

    canvas12.create_text(35,25, text="Grade #4", fill="white", font=('Helvetica 12 bold'))
    canvas12.grid(row=4, column=1)

    canvas17.create_text(40,25, text="Weight #1", fill="white", font=('Helvetica 12 bold'))
    canvas17.grid(row=1, column=2)

    canvas18.create_text(40,25, text="Weight #2", fill="white", font=('Helvetica 12 bold'))
    canvas18.grid(row=2, column=2)

    canvas19.create_text(40,25, text="Weight #3", fill="white", font=('Helvetica 12 bold'))
    canvas19.grid(row=3, column=2)

    canvas20.create_text(40,25, text="Weight #4", fill="white", font=('Helvetica 12 bold'))
    canvas20.grid(row=4, column=2)

    window.mainloop()