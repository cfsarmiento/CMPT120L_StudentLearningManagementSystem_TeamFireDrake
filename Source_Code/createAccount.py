'''
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
os.chdir(pathlib.Path(__file__).parent.resolve())
window=tk.Tk()
window.title('Create Account')
window.geometry('375x125')

def CreateAccount():
    username = usernameEntry.get()
    password = passwordEntry.get()
    confirm = confirmEntry.get()
    if (password == confirm):
        with open("account.csv", "w", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([username, password])
        window.destroy()
    else:
        errorLabel = tk.Label(window, text = "Passwords don't match", fg = 'black')
        errorLabel.grid(column = 2, row = 2)

usernameLabel=tk.Label(window, text = 'Set Username', fg = 'black')
usernameLabel.grid(column = 0, row = 0)
passwordLabel=tk.Label(window, text = 'Set Password', fg = 'black')
passwordLabel.grid(column = 0, row = 1)
confirmLabel=tk.Label(window, text = 'Confirm Password', fg = 'black')
confirmLabel.grid(column = 0, row = 2)

usernameEntry=tk.Entry(window, bg = 'grey')
usernameEntry.grid(row = 0, column = 1)

passwordEntry=tk.Entry(window, bg = 'grey')
passwordEntry.grid(row = 1, column = 1)

confirmEntry=tk.Entry(window, bg = 'grey')
confirmEntry.grid(row = 2, column = 1)

createAccountButton=tk.Button(window, bg = 'grey', text = 'Create Account', command = CreateAccount)
createAccountButton.grid(column = 1, row = 3, pady = 20)

window.mainloop()