'''
***this is a copy saved in the precise name needed to import the file...***
Title: Create Account
Window: Create Account Window
Author: Ethan Morton
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Create a username and password and store it in a csv file
Widgets:
    labels: username, password, confirm password
    entries: username, password, confirm password
    buttons: create account
Other Requirements: TKInter for Interface Design.
'''
import tkinter as tk
from tkinter import *
import os
import csv
import pathlib
os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts"))
window=tk.Tk()
window.configure(bg='grey')
window.title('Create Account')
window.geometry('375x130')

def CreateAccount():
    username = usernameEntry.get()
    password = passwordEntry.get()
    confirm = confirmEntry.get()
    accountFolders = list[int]()
    for path in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), path)):
            if (len(accountFolders) == 0):
                accountFolders.append(path)
            for folder in accountFolders:
                pathNum = int(path[path.index("t")+1:])
                folderNum = int(folder[folder.index("t")+1:])
                if (pathNum > folderNum):
                    accountFolders.insert(accountFolders.index(folder)+1, pathNum)
    firstAvailableNum = len(accountFolders)
    for i, folder in enumerate(accountFolders):
        if (folder != i):
            firstAvailableNum = i
            break
    os.makedirs(os.path.join(os.getcwd(), "Account" + str(firstAvailableNum)))
    os.chdir(os.path.join(os.getcwd(), "Account" + str(firstAvailableNum)))
    if (password == confirm):
        with open("loginInfo.csv", "w", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([username, password])
        window.destroy()
    else:
        errorLabel = tk.Label(window, text = "Passwords don't match", fg = 'white', bg='grey', font='Helvetica 12 bold')
        errorLabel.grid(column = 2, row = 2)

usernameLabel=tk.Label(window, text = 'Set Username: ', fg = 'white', bg='grey', font='Helvetica 12 bold')
usernameLabel.grid(column = 0, row = 0)
passwordLabel=tk.Label(window, text = 'Set Password: ', fg = 'white', bg='grey', font='Helvetica 12 bold')
passwordLabel.grid(column = 0, row = 1)
confirmLabel=tk.Label(window, text = 'Confirm Password: ', fg = 'white', bg='grey', font='Helvetica 12 bold')
confirmLabel.grid(column = 0, row = 2)

usernameEntry=tk.Entry(window, bg = 'grey', fg='white', font='Helvetica 12 bold')
usernameEntry.grid(row = 0, column = 1)

passwordEntry=tk.Entry(window, bg = 'grey', fg='white', font='Helvetica 12 bold')
passwordEntry.grid(row = 1, column = 1)

confirmEntry=tk.Entry(window, bg = 'grey', fg='white', font='Helvetica 12 bold')
confirmEntry.grid(row = 2, column = 1)

createAccountButton=tk.Button(window, bg = 'grey', fg='white', font='Helvetica 12 bold', text = 'Create Account', command = CreateAccount)
createAccountButton.grid(column = 1, row = 3, pady = 20)

window.mainloop()
