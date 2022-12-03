'''
Title: Potential GPA Calculator
Window: Potential GPA Calculator Window
Author: Ethan Morton and Paul Bergeron
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Allow users to calculate their potential gpa
Other Requirements: TKInter for Interface Design.
'''
def POTENTIAL_GPA_CALCULATOR():
    import tkinter as tk
    window=tk.Tk()
    window.title('Potential GPA Calculator')
    window.geometry('675x400')
    window.configure(bg='grey')

    def Back():
        window.destroy()
        import mainPage
        mainPage.MAIN_PAGE()

    def Calculate():
        import sourceCodeLibrary
        classGPAs = 0
        classCredits = 0
        for entries in classes:
            try:
                classGPAs += sourceCodeLibrary.GradeToGPA(float(entries[1].get())) * float(entries[2].get())
                classCredits += float(entries[2].get())
            except:
                gpalab.configure(text = "Your Grade and Credits must be numbers.")
                return
        try:
            classGPAs /= classCredits
        except:
            classGPAs = 0
        gpalab.configure(text = "Potential Gpa: {:0.2f}".format(classGPAs))

    def AddClass():
        classes.append([tk.Entry(window,bg='grey'), tk.Entry(window,bg='grey'), tk.Entry(window,bg='grey')])
        classes[-1][0].grid(row=len(classes)+1,column=0)
        classes[-1][1].grid(row=len(classes)+1,column=1)
        classes[-1][2].grid(row=len(classes)+1,column=2)
        addClassButton.grid(row=len(classes)+2)
        calculateButton.grid(row=len(classes)+3)
        gpalab.grid(row=len(classes)+3)
        if (len(classes) >= 1):
            removeClassButtons.append(tk.Button(window,bg='grey',fg='white',text='Remove Class',font='Helvetica 12 bold',command=RemoveClass))
        if (len(removeClassButtons) > 1):
            removeClassButtons.pop(0).destroy()
        removeClassButtons[0].grid(column=3,row=len(classes)+1)

    def RemoveClass():
        classes[-1][0].destroy()
        classes[-1][1].destroy()
        classes[-1][2].destroy()
        classes.pop()
        addClassButton.grid(row=len(classes)+2)
        calculateButton.grid(row=len(classes)+3)
        gpalab.grid(row=len(classes)+3)
        removeClassButtons[0].grid(column=3,row=len(classes)+1)
        if (len(classes) == 0):
            removeClassButtons.pop().destroy()

    
    title1=tk.Label(window,text='Class',fg='white',font='Helvetica 12 bold',bg='grey')
    title1.grid(column=0,row=1)
    grade=tk.Label(window,text='Grade',fg='white',font='Helvetica 12 bold',bg='grey')
    grade.grid(column=1,row=1)
    credit=tk.Label(window,text='Credits',fg='white',font='Helvetica 12 bold',bg='grey')
    credit.grid(column=2,row=1)
    gpalab=tk.Label(window,text="Potential Gpa: ",fg='white',font='Helvetica 12 bold',bg='grey')
    gpalab.grid(column=2,row=3,pady=15)

    addClassButton=tk.Button(window,bg='grey',fg='white',text='Add Class',font='Helvetica 12 bold',command=AddClass)
    addClassButton.grid(column=0,row=2,pady=15)

    classes = []

    removeClassButtons = []

    calculateButton=tk.Button(window,bg='grey',fg='white',text='Calculate',font='Helvetica 12 bold',command=Calculate)
    calculateButton.grid(column=1,row=3,pady=15)

    backButton = tk.Button(window,text = 'Back',bg = 'grey', fg='white', font='Helvetica 12 bold',padx = 55,command = Back)
    backButton.grid(row = 0, column = 3)

    window.mainloop()
