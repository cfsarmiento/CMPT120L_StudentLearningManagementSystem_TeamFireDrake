import tkinter as tk
from tkinter import *
import os
import csv
import pathlib
os.chdir(pathlib.Path(__file__).parent.resolve())
window=tk.Tk()
window.configure(bg='grey')
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
