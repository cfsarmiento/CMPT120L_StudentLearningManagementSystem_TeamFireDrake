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
import tkinter as tk

# Window
drop_withdrawl = tk.Tk()
drop_withdrawl.title('Drop/Withdrawl')  # title for window
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

# Buttons for Classes
test_classes = ['DATA 300', 'CMPT 220L', 'MATH 280', 'ECON 103L'] # actual data from backend
count = 0
for c in test_classes:
    tk.Button(classSelectionFrame,text = c,bg = 'grey',fg = 'white',font = 'Helvetica 12 bold').grid(row = count, column = 1)
    count = count+1
            
# Buttons for Dropping and Withdrawling
btnDrop = tk.Button(dropWithdrawlFrame, text = 'Drop', fg='white', bg='grey', font='Helvetica 12 bold')
btnDrop.grid(row = 0, column = 0)

btnWithdrawl = tk.Button(dropWithdrawlFrame, text = 'Withdrawl', fg='white', bg='grey', font='Helvetica 12 bold')
btnWithdrawl.grid(row = 0, column = 1)

# Button to Apply Changes
btnApplyChanges = tk.Button(drop_withdrawl, text = 'Finalize', fg='white', bg='grey', font='Helvetica 12 bold')
btnApplyChanges.grid(row = 4, column = 9)

drop_withdrawl.mainloop()
