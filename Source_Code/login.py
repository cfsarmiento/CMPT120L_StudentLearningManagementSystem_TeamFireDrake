'''
Title: Login
Window: Login Window
Author: Ethan Morton
Class: CMPT120L
Professor: Reza Sadeghi
Goal: Enter username and password correctly to access the program
Widgets:
    labels: username, password
    entries: username, password
    buttons: login, create account
Other Requirements: TKInter for Interface Design.
'''
import tkinter as tk
from tkinter import *
import os
import csv
import pathlib
os.chdir(pathlib.Path(__file__).parent.resolve())
window=tk.Tk()
window.title('Login')
window.geometry('375x150')

def Login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    with open("account.csv", "r", newline = "") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if (username == line[0] and password == line[1]):
                #import mainPage            # it would be easier to take spaces out of file names
                #__import__("Main Page")    # this method should work too if we have to use it
                pass                        # don't forget to remove the pass
            else:
                errorLabel = tk.Label(window, text = "Username or password incorrect", fg = 'black')
                errorLabel.grid(column = 2, row = 1)

def CreateAccount():
    import createAccount

usernameLabel=tk.Label(window, text = 'Username', fg = 'black')
usernameLabel.grid(column = 0, row = 0)
passwordLabel=tk.Label(window, text = 'Password', fg = 'black')
passwordLabel.grid(column = 0, row = 1)

usernameEntry=tk.Entry(window, bg = 'grey')
usernameEntry.grid(row = 0, column = 1)

passwordEntry=tk.Entry(window, bg = 'grey')
passwordEntry.grid(row = 1, column = 1)

loginButton=tk.Button(window, bg = 'grey', text = 'Login', command = Login)
loginButton.grid(column = 1, row = 3, pady = 20)

createAccountButton=tk.Button(window, bg = 'grey', text = 'Create Account', command = CreateAccount)
createAccountButton.grid(column = 1, row = 4)

window.mainloop()