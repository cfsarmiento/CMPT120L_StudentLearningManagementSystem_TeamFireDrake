import tkinter as tk
window = tk.Tk()
window.title('Finalize Semester')
window.geometry('550x80')
window.configure(bg = "grey")

descriptionText0 = tk.Label(window, text = "Finalize the information in this previous semester?", bg = "black", fg = 'white', font='Helvetica 12 bold')
descriptionText0.grid(column = 1, row = 0)

descriptionText1 = tk.Label(window, text = "This is permanent and you cannot go back to edit.", bg = "black", fg = 'red', font='Helvetica 12 bold')
descriptionText1.grid(column = 1, row = 1)

cancelButton = tk.Button(window, bg = "red", fg = "white", text = "Cancel", font='Helvetica 12 bold')
cancelButton.grid(column = 0, row = 2)

saveButton = tk.Button(window, bg = "green", fg = "white", text = "Finalize", font='Helvetica 12 bold')
saveButton.grid(column = 2, row = 2)

window.mainloop()
