'''
Title: Add Class
Window: Add Class Window
Author: Ethan Morton
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Add a class to track for the calculator
Widgets: labels and buttons
Other Requirements: TKInter for Interface Design.
'''
import tkinter as tk
from tkinter import *
import os
import csv
import pathlib
os.chdir(pathlib.Path(__file__).parent.resolve())
window=tk.Tk()
window.title('Add Class')
window.geometry('400x150')

def Homework():
    if homeworkButton["bg"] == "green":
        homeworkButton.configure(bg="orange")
    else:
        homeworkButton.configure(bg="green")

def Test():
    if testButton["bg"] == "green":
        testButton.configure(bg="orange")
    else:
        testButton.configure(bg="green")

def Project():
    if projectButton["bg"] == "green":
        projectButton.configure(bg="orange")
    else:
        projectButton.configure(bg="green")

def Quiz():
    if quizButton["bg"] == "green":
        quizButton.configure(bg="orange")
    else:
        quizButton.configure(bg="green")

def Essay():
    if essayButton["bg"] == "green":
        essayButton.configure(bg="orange")
    else:
        essayButton.configure(bg="green")

def Credit1():
    credit1Button.configure(bg="orange")
    credit3Button.configure(bg="green")
    credit4Button.configure(bg="green")

def Credit3():
    credit1Button.configure(bg="green")
    credit3Button.configure(bg="orange")
    credit4Button.configure(bg="green")

def Credit4():
    credit1Button.configure(bg="green")
    credit3Button.configure(bg="green")
    credit4Button.configure(bg="orange")

def AddClass():
    # save class info to classes.csv
    # talk to Christian about format
    courseAbbr = courseAbbrEntry.get()
    homework = homeworkEntry.get()
    test = testEntry.get()
    project = projectEntry.get()
    quiz = quizEntry.get()
    essay = essayEntry.get()
    credits = 0
    if (credit1Button["bg"] == "orange"):
        credits = 1
    elif (credit3Button["bg"] == "orange"):
        credits = 3
    elif (credit4Button["bg"] == "orange"):
        credits = 4
    types = []
    if (homeworkButton["bg"] == "orange"):
        types.append("Homework: " + str(homework))
    if (testButton["bg"] == "orange"):
        types.append("Test: " + str(test))
    if (projectButton["bg"] == "orange"):
        types.append("Project: " + str(project))
    if (quizButton["bg"] == "orange"):
        types.append("Quiz: " + str(quiz))
    if (essayButton["bg"] == "orange"):
        types.append("Essay: " + str(essay))
    classInfo = ["Course: " + courseAbbr, "Credits: " + str(credits)]
    classInfo.extend(types)
    with open(f"course{courseAbbr}.csv", "w", newline = "") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(classInfo)
    window.destroy()

labelFrame = tk.Frame(window)
labelFrame.grid(row = 0, column = 0)
secondFrame = tk.Frame(window)
secondFrame.grid(row = 1, column = 0)
buttonFrame = tk.Frame(window)
buttonFrame.grid(row = 2, column = 0)
bottomFrame = tk.Frame(window)
bottomFrame.grid(row = 3, column = 0)
creditsFrame = tk.Frame(bottomFrame)
creditsFrame.grid(row = 1, column = 1)

courseAbbrLabel = tk.Label(labelFrame, text = 'Subject and Course Number (e.g. CMPT_120):', fg = 'black')
courseAbbrLabel.grid(column = 0, row = 0)
courseAbbrEntry = tk.Entry(labelFrame, bg = 'grey')
courseAbbrEntry.grid(column = 1, row = 0)

assignmentTypeLabel = tk.Label(secondFrame, text = 'Click the assignment types that apply, then enter the weight for that type.', fg = 'black')
assignmentTypeLabel.grid(column = 0, row = 0)

homeworkButton=tk.Button(buttonFrame, bg = 'green', text = 'Homework', width = 10, command = Homework)
homeworkButton.grid(column = 0, row = 0)
homeworkEntry = tk.Entry(buttonFrame, bg = 'grey', width = 12)
homeworkEntry.grid(column = 0, row = 1)

testButton=tk.Button(buttonFrame, bg = 'green', text = 'Test', width = 10, command = Test)
testButton.grid(column = 1, row = 0)
testEntry = tk.Entry(buttonFrame, bg = 'grey', width = 12)
testEntry.grid(column = 1, row = 1)

projectButton=tk.Button(buttonFrame, bg = 'green', text = 'Project', width = 10, command = Project)
projectButton.grid(column = 2, row = 0)
projectEntry = tk.Entry(buttonFrame, bg = 'grey', width = 12)
projectEntry.grid(column = 2, row = 1)

quizButton=tk.Button(buttonFrame, bg = 'green', text = 'Quiz', width = 10, command = Quiz)
quizButton.grid(column = 3, row = 0)
quizEntry = tk.Entry(buttonFrame, bg = 'grey', width = 12)
quizEntry.grid(column = 3, row = 1)

essayButton=tk.Button(buttonFrame, bg = 'green', text = 'Essay', width = 10, command = Essay)
essayButton.grid(column = 4, row = 0)
essayEntry = tk.Entry(buttonFrame, bg = 'grey', width = 12)
essayEntry.grid(column = 4, row = 1)

creditsLabel = tk.Label(bottomFrame, text = 'Class Credits:', fg = 'black')
creditsLabel.grid(column = 0, row = 1)

credit1Button = tk.Button(creditsFrame, bg = 'green', text = '1', command = Credit1)
credit1Button.grid(column = 0, row = 0)

credit3Button = tk.Button(creditsFrame, bg = 'green', text = '3', command = Credit3)
credit3Button.grid(column = 1, row = 0)

credit4Button = tk.Button(creditsFrame, bg = 'green', text = '4', command = Credit4)
credit4Button.grid(column = 2, row = 0)

addButton = tk.Button(bottomFrame, bg = 'green', text = 'Add Class', command = AddClass)
addButton.grid(column = 0, row = 2)

window.mainloop()