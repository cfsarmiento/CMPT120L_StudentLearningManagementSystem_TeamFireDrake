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
def LOGIN():
    import tkinter as tk
    import os
    import csv
    import pathlib
    os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts"))
    window=tk.Tk()
    window.configure(bg='grey')
    window.title('Login')
    window.geometry('500x160')

    def Login():
        username = usernameEntry.get()
        password = passwordEntry.get()
        loginFound = False
        accountFile = ""
        for path in os.listdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts")):
            if os.path.isdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", path)):
                os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", path))
                with open("loginInfo.csv", "r", newline = "") as csvfile:
                    reader = csv.reader(csvfile)
                    for line in reader:
                        if (username == line[0] and password == line[1]):
                            loginFound = True
                            accountFile = path
                            break
            if (loginFound):
                break
        if (loginFound):
            os.chdir(pathlib.Path(__file__).parent.resolve())
            with open("currentLogin.csv", "w", newline = "") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([accountFile, "GPA: 0"])
            import sourceCodeLibrary
            if os.path.exists("semesterInfo.csv"):
                sourceCodeLibrary.CalculateCumulativeGPA()
            window.destroy()
            import mainPage
            mainPage.MAIN_PAGE()
        else:
            errorLabel = tk.Label(window, text = "Username or password incorrect", fg = 'black')
            errorLabel.grid(column = 2, row = 1)

    def CreateAccount():
        window.destroy()
        import createAccount
        createAccount.CREATE_ACCOUNT()

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