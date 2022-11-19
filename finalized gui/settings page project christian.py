import tkinter as tk
window = tk.Tk()
window.title('Settings')
window.geometry('300x100')
window.configure(bg = "grey")

addClassButton = tk.Button(window, bg = "grey", fg = "white", text = "Add Class", padx=22)
addClassButton.grid(column = 1, row = 1)
addClassButton.place(x=100, y=10)

removeClassButton = tk.Button(window, bg = "grey", fg = "white", text = "Remove Class", padx=11)
removeClassButton.grid(column = 1, row = 2)
removeClassButton.place(x=100, y=35)

semesterSettingsButton = tk.Button(window, bg = "grey", fg = "white", text = "Semester Settings")
semesterSettingsButton.grid(column = 1, row = 3)
semesterSettingsButton.place(x=100, y=60)

window.mainloop()
