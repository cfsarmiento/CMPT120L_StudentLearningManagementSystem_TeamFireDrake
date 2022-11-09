'''
Title: Student Learning Management System
Window: Drop/Withdrawl Window
Author: Christian Sarmiento
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Allows user to drop or withdraw from a class they are currently enrolled and taking
Widgets:   
Other Requirements: TKInter for Interface Design.
'''

# Import Libraries
import tkinter as tk

# Window
drop_withdrawl = tk.Tk()
drop_withdrawl.title('Drop/Withdrawl')  # title for window
drop_withdrawl.geometry('300x300')  # length x width
drop_withdrawl.configure(bg = 'white')  # background color

# Frames
classSelectionFrame = tk.Frame(drop_withdrawl, bg = 'red', width = 200, height = 100)
dropWithdrawlFrame = tk.Frame(drop_withdrawl, bg = 'red' , height = 50, width = 300)

classSelectionFrame.grid(row = 1, column = 5)
dropWithdrawlFrame.grid(row = 2, column = 5)
# Label for Select a Class
selectClassLabel = tk.Label(drop_withdrawl,
                            text = 'Select a Class',
                            bg = 'white',
                            fg = 'black',
                            padx = 30,
                            pady = 30)
selectClassLabel.grid(row = 0, column = 5)

# Buttons for Classes
test_classes = ['DATA 300', 'CMPT 220L', 'MATH 280', 'ECON 103L'] # actual data from backend
for c in test_classes:
    for i in range(len(test_classes)):  # Gets Button for Each Class
        tk.Button(classSelectionFrame,
                  text = c,
                  bg = 'lightgrey',
                  fg = 'black').grid(row = i, column = 1)
            
# Buttons for Dropping and Withdrawling
btnDrop = tk.Button(dropWithdrawlFrame, text = 'Drop')
btnDrop.grid(row = 0, column = 0)

btnWithdrawl = tk.Button(dropWithdrawlFrame, text = 'Withdrawl')
btnWithdrawl.grid(row = 0, column = 1)

# Button to Apply Changes
btnApplyChanges = tk.Button(drop_withdrawl, text = 'Apply')
btnApplyChanges.grid(row = 4, column = 9)

drop_withdrawl.mainloop()
