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
def ADD_CLASS():
    import tkinter as tk
    import os
    import csv
    import sourceCodeLibrary
    mostRecentSemesterDirectory = sourceCodeLibrary.GetMostRecentSemesterDirectory()
    os.chdir(mostRecentSemesterDirectory)

    window=tk.Tk()
    window.configure(bg='grey')
    window.title('Add Class')
    window.geometry('600x200')
    
    def Credit1():
        credit1Button.configure(bg="orange")
        credit3Button.configure(bg="black")
        credit4Button.configure(bg="black")

    def Credit3():
        credit1Button.configure(bg="black")
        credit3Button.configure(bg="orange")
        credit4Button.configure(bg="black")

    def Credit4():
        credit1Button.configure(bg="black")
        credit3Button.configure(bg="black")
        credit4Button.configure(bg="orange")

    def AddClass():
        courseAbbr = courseAbbrEntry.get()
        credits = 0
        if (credit1Button["bg"] == "orange"):
            credits = 1
        elif (credit3Button["bg"] == "orange"):
            credits = 3
        elif (credit4Button["bg"] == "orange"):
            credits = 4
        if (courseAbbr == "" or credits == 0):
            errorLabel.configure(text='Please choose a name and credits')
            return
        classInfo = ["Course: " + courseAbbr, "Credits: " + str(credits), "Grade: 0"]
        with open(f"course{courseAbbr}.csv", "w", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(classInfo)
        import sourceCodeLibrary
        sourceCodeLibrary.CalculateSemesterGPA()
        window.destroy()
        import mainPage
        mainPage.MAIN_PAGE()

    def Back():
        window.destroy()
        import mainPage
        mainPage.MAIN_PAGE()

    labelFrame = tk.Frame(window, bg='grey')
    labelFrame.grid(row = 0, column = 0)
    secondFrame = tk.Frame(window,bg='grey')
    secondFrame.grid(row = 1, column = 0)
    buttonFrame = tk.Frame(window,bg='grey')
    buttonFrame.grid(row = 2, column = 0)
    bottomFrame = tk.Frame(window,bg='grey')
    bottomFrame.grid(row = 3, column = 0)
    creditsFrame = tk.Frame(bottomFrame,bg='grey')
    creditsFrame.grid(row = 1, column = 1)

    courseAbbrLabel = tk.Label(labelFrame, text = 'Subject and Course Number (e.g. CMPT_120):', fg = 'white', bg='grey', font='Helvetica 12 bold' )
    courseAbbrLabel.grid(column = 0, row = 0)
    courseAbbrEntry = tk.Entry(labelFrame, bg = 'lightgrey')
    courseAbbrEntry.grid(column = 1, row = 0)
    
    creditsLabel = tk.Label(bottomFrame, text = 'Class Credits:', font='Helvetica 12 bold', fg='white',bg = 'grey')
    creditsLabel.grid(column = 0, row = 1)

    credit1Button = tk.Button(creditsFrame, bg = 'black', fg='white',font='Helvetica 12 bold',text = '1', command = Credit1)
    credit1Button.grid(column = 0, row = 0)

    credit3Button = tk.Button(creditsFrame, bg = 'black', fg='white',font='Helvetica 12 bold',text = '3', command = Credit3)
    credit3Button.grid(column = 1, row = 0)

    credit4Button = tk.Button(creditsFrame, bg = 'black', fg='white',font='Helvetica 12 bold',text = '4', command = Credit4)
    credit4Button.grid(column = 2, row = 0)

    errorLabel = tk.Label(bottomFrame, text = "", font='Helvetica 12 bold', fg='white',bg = 'grey')
    errorLabel.grid(column = 0, row = 2)

    addButton = tk.Button(bottomFrame, bg = 'black', fg='white',font='Helvetica 12 bold',text = 'Add Class', command = AddClass)
    addButton.grid(column = 0, row = 3)

    backButton = tk.Button(bottomFrame, bg = 'black', fg='white',font='Helvetica 12 bold',text = 'Back', command = Back)
    backButton.grid(column = 0, row = 4)

    window.mainloop()