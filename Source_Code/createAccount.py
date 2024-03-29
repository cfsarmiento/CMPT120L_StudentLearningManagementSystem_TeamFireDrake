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
def CREATE_ACCOUNT():
    import tkinter as tk
    import os
    import csv
    import pathlib
    os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts"))
    window=tk.Tk()
    window.configure(bg='grey')
    window.title('Create Account')
    window.geometry('600x150')

    def CreateAccount():
        username = usernameEntry.get()
        password = passwordEntry.get()
        confirm = confirmEntry.get()
        accountFolders = list[int]()
        for account in os.listdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts")):
            if (os.path.isdir(os.path.join(os.getcwd(), account)) and account[0:7] == "Account"):
                os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", account))
                with open("loginInfo.csv", "r", newline="") as csvfile:
                    reader = csv.reader(csvfile)
                    for line in reader:
                        if (username == line[0]):
                            error1Label = tk.Label(window, text = "Username already exists", fg = 'white', bg='grey', font='Helvetica 12 bold')
                            error1Label.grid(column = 2, row = 1)
                            return
                        break
                os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts"))
                accountNum = int(account[7:])
                if (len(accountFolders) == 0):
                    accountFolders.append(accountNum)
                for num in accountFolders:
                    if (accountNum < num):
                        accountFolders.insert(accountFolders.index(num), accountNum)
                    elif (accountNum > num):
                        accountFolders.insert(accountFolders.index(num)+1, accountNum)
        firstAvailableNum = len(accountFolders)
        for i, folder in enumerate(accountFolders):
            if (folder != i):
                firstAvailableNum = i
                break
        if (password == confirm):
            os.makedirs(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", "Account" + str(firstAvailableNum)))
            os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", "Account" + str(firstAvailableNum)))
            with open("loginInfo.csv", "w", newline = "") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([username, password, "GPA: 0"])
            os.makedirs("Semesters")
            window.destroy()
            import login
            login.LOGIN()
        else:
            error2Label = tk.Label(window, text = "Passwords don't match", fg = 'white', bg='grey', font='Helvetica 12 bold')
            error2Label.grid(column = 2, row = 2)

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