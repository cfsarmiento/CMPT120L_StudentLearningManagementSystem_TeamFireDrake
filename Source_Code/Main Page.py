'''
Name: Michael McMahon
Title: Main Page
Goal: Print out a main page and to create buttons that direct to other pages
OR: Use tkinter for GUI
'''
import tkinter as tk
window=tk.Tk()
window.title("Main Page")
window.geometry("500x500")
window.config(bg="Gray")

frame1=tk.Frame(window,bg="Gray",highlightbackground="White",highlightthickness=1,width=249,height=249)
frame1.grid(row=0,column=0)
tk.Label(window,bg="Gray",fg="White",text="SLMS",font='Helvetica 40 bold').grid(row=0,column=0)

frame2=tk.Frame(window,bg="Gray",width=250,height=250)
frame2.grid(row=0,column=1)
tk.Button(frame2,bg="Gray",fg="White",text="Course Settings",font='Helvetica 12 bold',command=courseSetting).grid(row=0,column=0,pady=10)
tk.Button(frame2,bg="Gray",fg="White",text="Add/Edit Grade",font='Helvetica 12 bold').grid(row=1,column=0)

frame3=tk.Frame(window,bg="Gray",width=249,height=249)
frame3.grid(row=1,column=0)
tk.Button(frame3,bg="Gray",fg="White",text="Cummulative Runtime",font='Helvetica 12 bold').grid(row=0,column=0,pady=10)
tk.Button(frame3,bg="Gray",fg="White",text="Potential GPA Calc",font='Helvetica 12 bold').grid(row=1,column=0)
num=1
for i in range(1,6):
    tk.Button(frame3,bg="Gray",fg="White",text="Class "+str(num),font='Helvetica 12 bold').grid(row=3+num,column=0,pady=5)
    num+=1

frame4=tk.Frame(window,bg="Gray",highlightbackground="White",highlightthickness=1,width=270,height=300)
frame4.grid(row=1,column=1)

window.mainloop()
