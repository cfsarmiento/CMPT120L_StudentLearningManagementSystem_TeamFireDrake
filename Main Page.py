'''
Author: Michael McMahon
Title: Main Page
Date: November 9, 2022
Goal: Print out a main page and to create buttons that direct to other pages
OR: Use tkinter for interface design
'''

import tkinter as tk
window=tk.Tk()
window.geometry("500x450")
window.config(bg="Black")

frame1=tk.Frame(window,bg="Black",highlightbackground="White",highlightthickness=1,width=80,height=50)
frame1.grid(row=0,column=0)
tk.Label(window,text="SLMS").grid(row=0,column=0)

frame2=tk.Frame(window,bg="Black",width=420,height=50)
frame2.grid(row=0,column=1)
tk.Button(frame2,text="Course Settings").grid(row=0,column=0,padx=35,pady=10)
tk.Button(frame2,text="Add/Edit Grade").grid(row=0,column=1,padx=35,pady=10)

frame3=tk.Frame(window,bg="Black",highlightbackground="White",highlightthickness=1,width=80,height=400)
frame3.grid(row=1,column=0)
tk.Button(frame3,text="Cummulative Random").grid(row=0,column=0,padx=20,pady=5)
tk.Button(frame3,text="Potential GPA Calc").grid(row=1,column=0,padx=20,pady=5)
num=1
for i in range(1,6):
    tk.Button(frame3,text="Class "+str(num)).grid(row=3+num,column=0,padx=20,pady=5)
    num+=1

frame4=tk.Frame(window,bg="Black",highlightbackground="White",highlightthickness=1,width=320,height=350)
frame4.grid(row=1,column=1)

window.mainloop()
