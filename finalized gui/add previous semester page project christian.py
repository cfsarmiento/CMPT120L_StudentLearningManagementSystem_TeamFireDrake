import tkinter as tk

# Window
semester_settings = tk.Tk()
semester_settings.title('Add Previous Semester')  # title for window
semester_settings.geometry('400x250')  # window size
semester_settings.configure(bg ='grey')  # color

# Frames
inputFrame = tk.Frame(semester_settings,
                      bg = 'grey',
                      width = 300,
                      height= 100)
newSemesterFrame = tk.Frame(semester_settings,
                            bg = 'grey',
                            width = 200,
                            height = 50)

inputFrame.grid(row = 1, column = 0)
newSemesterFrame.grid(row = 4, column = 0)

# Label for Add Past Final Semester GPA
addGPALabel = tk.Label(semester_settings,
                       text = 'Add a Past Final Semester GPA:',
                       bg = 'grey',
                       fg = 'white',
                       padx = 10,
                       pady = 10)
addGPALabel.grid(row = 0, column = 0)

# Label for Year Entry
yearLabel = tk.Label(inputFrame,
                     text = 'Year:',
                     bg = 'grey',
                     fg = 'white')
yearLabel.grid(row = 0, column = 0)

# Entry Window for Year
entryYear = tk.Entry(inputFrame,
                     bg = 'white')
entryYear.grid(row = 0, column = 1)

# Label for Session Entry
sessionLabel = tk.Label(inputFrame,
                     text = 'Session:',
                     bg = 'grey',
                     fg = 'white')
sessionLabel.grid(row = 1, column = 0)

# Entry Window for Session
entrySession = tk.Entry(inputFrame,
                     bg = 'white')
entrySession.grid(row = 1, column = 1)

# Label for Final GPA Entry
finalGPALabel = tk.Label(inputFrame,
                     text = 'Final GPA:',
                     bg = 'grey',
                     fg = 'white')
finalGPALabel.grid(row = 2, column = 0)

# Entry Window for Final GPA
entryFinalGPA = tk.Entry(inputFrame,
                     bg = 'white')
entryFinalGPA.grid(row = 2, column = 1)

# Button to Finalize Past GPA Entry
btnFinalize = tk.Button(inputFrame,
                        text = 'Finalize',
                        bg = 'grey',
                        fg = 'white',
                        padx = 55)
btnFinalize.grid(row = 3, column = 1)


                             
semester_settings.mainloop()
