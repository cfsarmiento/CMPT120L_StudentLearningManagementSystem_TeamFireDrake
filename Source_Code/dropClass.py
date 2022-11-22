'''
Title: Student Learning Management System
Window: Drop/Withdrawl Window
Authors: Ethan Morton
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Allows user to drop or withdraw from a class they are currently enrolled and taking
Widgets:   
Other Requirements: TKInter for Interface Design.
'''
def DROP_WITHDRAWL():
    import tkinter as tk
    import os
    import sourceCodeLibrary
    mostRecentSemesterDirectory = sourceCodeLibrary.GetMostRecentSemesterDirectory()
    os.chdir(mostRecentSemesterDirectory)

    def Search():
        course = searchEntry.get()
        classFoundLabel.configure(text=course+" not found")
        for file in os.listdir(mostRecentSemesterDirectory):
            if (course in file):
                classFoundLabel.configure(text=course+" found")
    
    def Drop():
        course=searchEntry.get()
        try:
            os.remove("course"+course+".csv")
            drop_withdrawl.destroy()
            import adjustCurrentSemester
            adjustCurrentSemester.ADJUST_CURRENT_SEMESTER()
        except:
            classFoundLabel.configure(text="Could not drop "+course)

    def Back():
        drop_withdrawl.destroy()
        import adjustCurrentSemester
        adjustCurrentSemester.ADJUST_CURRENT_SEMESTER()

    # Window
    drop_withdrawl = tk.Tk()
    drop_withdrawl.title('Drop')  # title for window
    drop_withdrawl.geometry('450x300')  # length x width
    drop_withdrawl.configure(bg = 'grey')  # background color

    searchFrame = tk.Frame(drop_withdrawl,bg = "Gray")
    searchFrame.grid(row=0, column=0)

    searchLabel = tk.Label(searchFrame, bg = "Gray", fg = "White", text = "Search the class you want to drop:", font = 'Helvetica 12 bold')
    searchLabel.grid(row = 0, column = 0)
    searchEntry = tk.Entry(searchFrame, bg = 'Gray')
    searchEntry.grid(row = 1, column = 0)

    searchButton = tk.Button(drop_withdrawl,bg="grey",fg="white",text="Search",font='Helvetica 12 bold', command=Search)
    searchButton.grid(row = 0, column = 1)

    classFoundLabel = tk.Label(drop_withdrawl, bg = "Gray", fg = "White", text = "", font = 'Helvetica 12 bold')
    classFoundLabel.grid(row = 1, column = 0)

    dropButton = tk.Button(drop_withdrawl,bg="grey",fg="white",text="Drop this course",font='Helvetica 12 bold', command= Drop)
    dropButton.grid(row = 2, column = 0)

    # Back Button
    btnBack = tk.Button(drop_withdrawl, text = 'Back', fg='white', bg='grey', font='Helvetica 12 bold', command=Back)
    btnBack.grid(row = 3, column = 0)

    drop_withdrawl.mainloop()
