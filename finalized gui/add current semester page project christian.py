import tkinter as tk

# Window
new_semester = tk.Tk()
new_semester.title('Add Current Semester') # title
new_semester.geometry('250x150')  # window dimensions
new_semester.configure(bg = 'grey')  # color

# Frames
newSemesterFrame = tk.Frame(new_semester,
                            bg = 'grey',
                            width = 100,
                            height = 50)
newSemesterFrame.grid(row = 1, column = 0)

# Label for Creating a New Semester
createSemesterLabel = tk.Label(new_semester,
                               text = 'Create Current Semester:',
                               bg = 'grey',
                               fg = 'white',
                               font = 'Helvetica 12 bold',
                               padx = 20,
                               pady = 10)
createSemesterLabel.grid(row = 0, column = 0)

# Label for Inputting New Semester Year
newYearLabel = tk.Label(newSemesterFrame,
                        text = 'Year',
                        bg = 'grey',
                        fg = 'white',
                        font='Helvetica 12 bold')
newYearLabel.grid(row = 0, column = 0)

# Entry Window for Year
entryNewYear = tk.Entry(newSemesterFrame,
                        bg = 'grey')
entryNewYear.grid(row = 0, column = 1)

# Label for Inputting New Semester Session
newSessionLabel = tk.Label(newSemesterFrame,
                        text = 'Session',
                        bg = 'grey',
                        fg = 'white',
                        font ='Helvetica 12 bold')
newSessionLabel.grid(row = 1, column = 0)

# Entry Window for Session
entrySessionYear = tk.Entry(newSemesterFrame,
                            bg = 'grey')
entrySessionYear.grid(row = 1, column = 1)

# Button to Create New Semester
btnNewSemester = tk.Button(newSemesterFrame,
                           text = 'Create',
                           bg = 'grey', fg='white', font='Helvetica 12 bold',
                           padx = 55)
btnNewSemester.grid(row = 2, column = 1)

new_semester.mainloop()
