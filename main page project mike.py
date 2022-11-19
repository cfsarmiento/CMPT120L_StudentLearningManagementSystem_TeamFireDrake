import tkinter as tk
from tkinter import *
window=tk.Tk()
window.title("Main Page")
window.geometry("1000x500")
window.config(bg="Gray")

frame1=tk.Frame(window,bg="Gray",highlightbackground="White",highlightthickness=1,width=100,height=100)
frame1.grid(row=0,column=0)
tk.Label(window,bg="Gray",fg="White",text="SLMS",font='Helvetica 30 bold').grid(row=0,column=0)

frame2=tk.Frame(window,bg="Gray",width=500,height=250)
frame2.grid(row=0,column=1)
tk.Button(frame2,bg="Gray",fg="White",text="Course Settings",font='Helvetica 12 bold').grid(row=1, column=1)
tk.Button(frame2,bg="Gray",fg="White",text="Add/Edit Grade",font='Helvetica 12 bold').grid(row=1,column=0)

frame3=tk.Frame(window,bg="Gray",width=249,height=249)
frame3.grid(row=1,column=0)
tk.Button(frame3,bg="Gray",fg="White",text="Cummulative Rundown",font='Helvetica 12 bold').grid(row=0,column=0,pady=10)
tk.Button(frame3,bg="Gray",fg="White",text="Potential GPA Calc",font='Helvetica 12 bold').grid(row=1,column=0)
num=1
for i in range(1,6):
    tk.Button(frame3,bg="Gray",fg="White",text="Class "+str(num),font='Helvetica 12 bold').grid(row=3+num,column=0,pady=5)
    num+=1

frame4=tk.Frame(window,bg="Gray",highlightbackground="White",highlightthickness=1,width=500,height=300)
frame4.grid(row=1,column=1)
textBox1=Text(frame4, bg="Gray", fg="White").grid(row=1, column=0)
#textBox1.config(state='disabled')
frame4.mainloop()

window.mainloop()
