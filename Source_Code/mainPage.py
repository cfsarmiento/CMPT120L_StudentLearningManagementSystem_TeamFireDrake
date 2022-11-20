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
import tkinter as tk
from tkinter import *
import os
import csv
import pathlib
os.chdir(pathlib.Path(__file__).parent.resolve())
accountFile = ""
with open("currentLogin.csv", "r", newline = "") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        accountFile = line[0]
os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", accountFile))
if not os.path.exists("Semesters"):
    os.makedirs("Semesters")
os.chdir(os.path.join(os.getcwd(), "Semesters"))

window=tk.Tk()
window.title("Main Page")
window.geometry("1200x550")
window.config(bg="Gray")

def AddCurrentSemester():
    window.destroy()
    import addCurrentSemester

def AddPreviousSemester():
    window.destroy()
    import addPreviousSemester

def AdjustSemester():
    window.destroy()
    import adjustCurrentSemester
    
def CumulativeRundown():
    pass

def PotentialGPA_Calculator():
    window.destroy()
    import potentialGPACalc
    
frame1=tk.Frame(window,bg="Gray",highlightbackground="White",highlightthickness=1,width=100,height=100)
frame1.grid(row=0,column=0)
tk.Label(window,bg="Gray",fg="White",text="SLMS",font='Helvetica 30 bold').grid(row=0,column=0)

frame2=tk.Frame(window,bg="Gray",width=500,height=140)
frame2.grid(row=0,column=1)
label= tk.Label(bg="Gray", fg="White", text="Course Name:       Grade:       Status:       ", font='Helvetica 12 bold').grid(row=0,column=1)
label= tk.Label(bg="Gray", fg="White", text="Semester GPA:    \nCummulative GPA:     ", font='Helvetica 12 bold').grid(row=0,column=2)

frame3=tk.Frame(window,bg="Gray",width=249,height=249)
frame3.grid(row=1,column=0)

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
            mostRecentSortedSemesterFile = sem
        elif (sortedYear == mostRecentSortedYear):
            if (sortedSession > mostRecentSortedSession):
                mostRecentSortedSession = sortedSession
                mostRecentSortedSemesterFile = sem
        if (year == sortedYear):
            if (session > sortedSession):
                sortedSemesters.insert(semesters.index(sem)-1, semester)
                break
            continue
        elif (year > sortedYear):
            sortedSemesters.append(semester)
            break
count = -1
if (mostRecentSemesterFile != ""):
    for path in os.listdir(os.path.join(os.getcwd(), mostRecentSemesterFile)):
        if os.path.isfile(os.path.join(os.getcwd(), mostRecentSemesterFile, path)):
            count += 1

for i in range(1,count):    # this will get the number of classes in the most recent semester and iterate through that number
    tk.Button(frame3,bg="Gray",fg="White",text="Class "+str(i),font='Helvetica 12 bold').grid(row=3+i,column=0,pady=5)

frame4=tk.Frame(window,bg="Gray",highlightbackground="White",highlightthickness=1,width=500,height=100)
frame4.grid(row=1,column=1)
#textBox1=Text(frame4, bg="Gray", fg="White").grid(row=1, column=0)
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
ftsLabel = tk.Label(frame6, bg = 'grey', fg = 'White', text = 'First Time Setup Users:\n 1. Add Currest Semester Button\n2. Add Classes (Adjust Current Semester)\n3. Add Grades(Adjust Current Semester)\n4. Add Previous Semester GPA (if Applicable)',font = 'Helvetica 12 bold')
ftsLabel.grid(row=2,column=0,sticky = W)

# iterates through the files and prints the year, session, and gpa into the GUI
table = [[],[],[]]
i = 0
for i, semester in enumerate(sortedSemesters, start = 1):
    os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", accountFile, "Semesters", semester))
    with open("semesterInfo.csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            table[0].append(tk.Label(yearFrame, bg = "Gray", fg = "White", text = line[0][line[0].index(" ")+1:], font = 'Helvetica 12 bold').grid(row=i,column=0, sticky = W))
            table[1].append(tk.Label(semesterFrame, bg = "Gray", fg = "White", text = line[1][line[1].index(" ")+1:], font = 'Helvetica 12 bold').grid(row=i,column=0, sticky = W))
            table[2].append(tk.Label(gpaFrame, bg = "Gray", fg = "White", text = line[2][line[2].index(" ")+1:], font = 'Helvetica 12 bold').grid(row=i,column=0, sticky = W))

frame5=tk.Frame(window,bg="Gray", width=500,height=300)
frame5.grid(row=1, column=2)
tk.Button(frame5,bg="Gray",fg="White",text="Add Current Semester",font='Helvetica 12 bold', command = AddCurrentSemester).grid(row=0,column=2, pady=10)
tk.Button(frame5,bg="Gray",fg="White",text="Add Previous Semester",font='Helvetica 12 bold', command = AddPreviousSemester).grid(row=1, column=2, pady=5)
tk.Button(frame5,bg="Gray",fg="White",text="Adjust Current Semester",font='Helvetica 12 bold', command = AdjustSemester).grid(row=2,column=2, pady=10)
tk.Button(frame5,bg="Gray",fg="White",text="Cummulative Rundown",font='Helvetica 12 bold', command = CumulativeRundown).grid(row=3,column=2,pady=10)
tk.Button(frame5,bg="Gray",fg="White",text="Potential GPA Calc",font='Helvetica 12 bold', command = PotentialGPA_Calculator).grid(row=4,column=2)

window.mainloop()
