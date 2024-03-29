'''
Title: Add Class
Window: Add Class Window
Author: Ethan Morton
Class: CMPT120L
Professor: Reza Sadeghi
Goal: 
Widgets: 
Other Requirements: TKInter for Interface Design.
'''
from tkinter import *
def MAIN_PAGE():
    import tkinter as tk
    import os
    import csv
    import pathlib
    import sourceCodeLibrary
    dict = sourceCodeLibrary.GetAccountDirectory()
    os.chdir(os.path.join(dict["semestersPath"]))

    window=tk.Tk()
    window.title("Main Page")
    window.geometry("1200x650")
    window.config(bg="Gray")

    def AddCurrentSemester():
        window.destroy()
        import addCurrentSemester
        addCurrentSemester.ADD_CURRENT_SEMESTER()

    def AddPreviousSemester():
        window.destroy()
        import addPreviousSemester
        addPreviousSemester.ADD_PREVIOUS_SEMESTER()

    def AdjustSemester():
        if (len(os.listdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", dict["accountPath"], "Semesters"))) > 0):
            window.destroy()
            import adjustCurrentSemester
            adjustCurrentSemester.ADJUST_CURRENT_SEMESTER()
        else:
            errorLabel = tk.Label(frame5, text = 'You must add a semester before you add a class', bg='grey', font='Helvetica 12 bold',fg = 'white')
            errorLabel.grid(column=2,row=4)

    def PotentialGPA_Calculator():
        window.destroy()
        import potentialGPACalculator
        potentialGPACalculator.POTENTIAL_GPA_CALCULATOR()

    def Class(course):
        window.destroy()
        import classManager
        classManager.CLASS_MANAGER(course)
        
    frame1=tk.Frame(window,bg="Gray",highlightbackground="White",highlightthickness=1,width=100,height=100)
    frame1.grid(row=0,column=0)
    tk.Label(window,bg="Gray",fg="White",text="SLMS",font='Helvetica 30 bold').grid(row=0,column=0)

    frame2=tk.Frame(window,bg="Gray",width=500,height=140)
    frame2.grid(row=0,column=1)
    label= tk.Label(bg="Gray", fg="White", text="Cummulative GPA: {:0.2f}".format(float(dict["cumulativeGPA"])), font='Helvetica 12 bold')
    label.grid(row=0,column=2)

    frame3=tk.Frame(window,bg="Gray",width=249,height=249)
    frame3.grid(row=1,column=0)

    # this block of code includes the sourceCodeLibrary.import sourceCodeLibrary.GetMostRecentSemesterDirectory() function
    # but I don't want to call it here because I use this same for loop to sort the semesters in order
    semesters = os.listdir(os.getcwd())
    sortedSemesters = list[str]()
    mostRecentSemesterFile = ""
    mostRecentYear = 0
    mostRecentSession = 0   # 1 = fall, 2 = winter, 3 = spring, 4 = summer
    for semester in semesters:
        # for determining the most recent semester
        year = int(semester[semester.index("_")+1:semester.rindex("_")])
        session = 0
        match semester[semester.rindex("_")+1:].lower():
            case "fall":
                session = 1
            case "autumn":  # just in case anyone writes this
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
        # for sorting the semesters into a list in order of how recent they are
        mostRecentSortedYear = 0
        mostRecentSortedSession = 0
        if (len(sortedSemesters) == 0):
            sortedSemesters.append(semester)
        for sem in sortedSemesters:
            sortedYear = int(sem[sem.index("_")+1:sem.rindex("_")])
            sortedSession = 0
            match sem[sem.rindex("_")+1:].lower():
                case "fall":
                    sortedSession = 1
                case "autumn":
                    sortedSession = 1
                case "winter":
                    sortedSession = 2
                case "spring":
                    sortedSession = 3
                case "summer":
                    sortedSession = 4
            if (sortedYear > mostRecentSortedYear):
                mostRecentSortedYear = sortedYear
            elif (sortedYear == mostRecentSortedYear):
                if (sortedSession > mostRecentSortedSession):
                    mostRecentSortedSession = sortedSession
            if (year == sortedYear):
                if (session > sortedSession):
                    sortedSemesters.insert(semesters.index(sem)-1, semester)
                    break
                continue
            elif (year > sortedYear):
                sortedSemesters.append(semester)
                break
    
    #BUG it seems each button opens the same course page. I can't figure out how to make each button open a different course page
    for i, file in enumerate(os.listdir(os.path.join(os.getcwd(), mostRecentSemesterFile))):
        if (os.path.isfile(os.path.join(os.getcwd(), mostRecentSemesterFile, file)) and file != "semesterInfo.csv"):
            course = file[file.index("e")+1:file.rindex(".")]
            tk.Button(frame3,bg="Gray",fg="White",text=course,font='Helvetica 12 bold', command = lambda course = course: Class(course)).grid(row=4+i,column=0,pady=5)

    frame4=tk.Frame(window,bg="Gray",highlightbackground="White",highlightthickness=1,width=500,height=100)
    frame4.grid(row=1,column=1)
    yearFrame = tk.Frame(frame4, bg = "Gray", width = 166, height = 300, padx = 30)
    yearFrame.grid(row=0,column=0)
    semesterFrame = tk.Frame(frame4, bg = "Gray", width = 166, height = 300, padx = 30)
    semesterFrame.grid(row=0,column=1)
    gpaFrame = tk.Frame(frame4, bg = "Gray", width = 166, height = 300, padx = 30)
    gpaFrame.grid(row=0,column=2)

    yearLabel = tk.Label(yearFrame, bg = "Gray", fg = "White", text = "Year:", font = 'Helvetica 12 bold')
    yearLabel.grid(row=0,column=0, sticky = W)

    semesterLabel = tk.Label(semesterFrame, bg = "Gray", fg = "White", text = "Semester:", font = 'Helvetica 12 bold')
    semesterLabel.grid(row=0,column=0, sticky = W)

    gpaLabel = tk.Label(gpaFrame, bg = "Gray", fg = "White", text = "GPA:", font = 'Helvetica 12 bold')
    gpaLabel.grid(row=0,column=0, sticky = W)

    #first time setup
    frame6=tk.Frame(window,bg="Gray",highlightbackground="White",highlightthickness=1,width=500,height=150)
    frame6.grid(row=2,column=0)
    ftsLabel = tk.Label(frame6, bg = 'grey', fg = 'White', text = "First Time?\n\n1. Add Current Semester\n\t--> input info\n2. Adjust Current Semester\n\t--> Add Class\n\t\t--> input info\n3. That Class (left side)\n\t--> Add Assignment\n\t\t--> input info\n3. Add Previous Semester (if applicable)\n\t--> input info",font = 'Helvetica 12 bold', justify=LEFT)
    ftsLabel.grid(row=2,column=0,sticky = W)

    # iterates through the files and prints the year, session, and gpa into the GUI
    table = [[],[],[]]
    i = 0
    for i, semester in enumerate(sortedSemesters, start = 1):
        os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", dict["accountPath"], "Semesters", semester))
        with open("semesterInfo.csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                table[0].append(tk.Label(yearFrame, bg = "Gray", fg = "White", text = line[0][line[0].index(" ")+1:], font = 'Helvetica 12 bold').grid(row=i,column=0, sticky = W))
                table[1].append(tk.Label(semesterFrame, bg = "Gray", fg = "White", text = line[1][line[1].index(" ")+1:], font = 'Helvetica 12 bold').grid(row=i,column=0, sticky = W))
                table[2].append(tk.Label(gpaFrame, bg = "Gray", fg = "White", text = "{:0.2f}".format(float(line[2][line[2].index(" ")+1:])), font = 'Helvetica 12 bold').grid(row=i,column=0, sticky = W))

    frame5=tk.Frame(window,bg="Gray", width=500,height=300)
    frame5.grid(row=1, column=2)
    tk.Button(frame5,bg="Gray",fg="White",text="Add Current Semester",font='Helvetica 12 bold', command = AddCurrentSemester).grid(row=0,column=2, pady=10)
    tk.Button(frame5,bg="Gray",fg="White",text="Add Previous Semester",font='Helvetica 12 bold', command = AddPreviousSemester).grid(row=1, column=2, pady=5)
    tk.Button(frame5,bg="Gray",fg="White",text="Adjust Current Semester",font='Helvetica 12 bold', command = AdjustSemester).grid(row=2,column=2, pady=10)
    tk.Button(frame5,bg="Gray",fg="White",text="Potential GPA Calc",font='Helvetica 12 bold', command = PotentialGPA_Calculator).grid(row=3,column=2)

    window.mainloop()