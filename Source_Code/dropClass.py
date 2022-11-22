'''
Title: Student Learning Management System
Window: Drop/Withdrawl Window
Authors: Christian Sarmiento and Gabrielle Knapp
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
    
    def Drop(file):
        os.remove(file)
        drop_withdrawl.destroy()
        import adjustCurrentSemester
        adjustCurrentSemester.ADJUST_CURRENT_SEMESTER()

    def Back():
        drop_withdrawl.destroy()
        import adjustCurrentSemester
        adjustCurrentSemester.ADJUST_CURRENT_SEMESTER()

    # Window
    drop_withdrawl = tk.Tk()
    drop_withdrawl.title('Drop')  # title for window
    drop_withdrawl.geometry('300x300')  # length x width
    drop_withdrawl.configure(bg = 'grey')  # background color

    # Frames
    classSelectionFrame = tk.Frame(drop_withdrawl, bg = 'grey', width = 200, height = 100)
    dropWithdrawlFrame = tk.Frame(drop_withdrawl, bg = 'grey' , height = 50, width = 300)

    classSelectionFrame.grid(row = 1, column = 5)
    dropWithdrawlFrame.grid(row = 2, column = 5)
    # Label for Select a Class
    selectClassLabel = tk.Label(drop_withdrawl,
                                text = 'Select a Class: ',
                                bg = 'grey',
                                fg = 'white',
                                font = 'Helvetica 12 bold',
                                padx = 30,
                                pady = 30)
    selectClassLabel.grid(row = 0, column = 5)

    classButtons = list[tk.Button]()
    classFiles = list[str]()
    for i, file in enumerate(os.listdir(mostRecentSemesterDirectory)):
        if ("course" in file):
            course = file[file.index("e")+1:file.index(".")]
            classFiles.append(file)
            classButtons.append(tk.Button(classSelectionFrame,bg="grey",fg="white",text="Drop "+course,font='Helvetica 12 bold', command=lambda: Drop(classFiles[classFiles.index("course"+course+".csv")])).grid(row = i, column = 1))

    # Back Button
    btnBack = tk.Button(drop_withdrawl, text = 'Back', fg='white', bg='grey', font='Helvetica 12 bold', command=Back)
    btnBack.grid(row = 0, column = 0)

    drop_withdrawl.mainloop()