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
window.configure(bg='grey')
window.title('Login')
window.geometry('375x150')

def Login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    with open("account.csv", "r", newline = "") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if (username == line[0] and password == line[1]):
                import mainPage
            else:
                errorLabel = tk.Label(window, text = "Username or password incorrect", fg = 'black')
                errorLabel.grid(column = 2, row = 1)

def CreateAccount():
    import createAccount

usernameLabel=tk.Label(window, text = 'Username: ', bg='grey', fg = 'white', font='Helvetica 12 bold')
usernameLabel.grid(column = 0, row = 0)
passwordLabel=tk.Label(window, text = 'Password: ', bg='grey', fg = 'white', font='Helvetica 12 bold')
passwordLabel.grid(column = 0, row = 1)

usernameEntry=tk.Entry(window, bg = 'grey', fg='white', font="Helvetica 12 bold" )
usernameEntry.grid(row = 0, column = 1)

passwordEntry=tk.Entry(window, bg = 'grey', fg='white', font="Helvetica 12 bold")
passwordEntry.grid(row = 1, column = 1)

loginButton=tk.Button(window, bg = 'grey', fg='white', font= 'Helvetica 12 bold',text = 'Login', command = Login)
loginButton.grid(column = 1, row = 3, pady = 20)

createAccountButton=tk.Button(window, bg = 'grey', fg='white', font='Helvetica 12 bold', text = 'Create Account', command = CreateAccount)
createAccountButton.grid(column = 1, row = 4)

window.mainloop()