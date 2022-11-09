from tkinter import *

window=Tk()
window.title('Class Manager')
window.geometry('600x300')
window.configure(bg='black')


assignment = Label(window,bg='black',fg='white',font='Helvetica 12 bold', text="Assignment Type\n______\nHomework\n______\nTests\n______\nQuizzes\n______\nProjects\n______")
assignment.grid(row=0,column=0)


grade = Label(window,bg='black',fg='white',font='Helvetica 12 bold',text="Grade\n______\nAverage Grade\n______\nAverage Grade\n______\nAverage Grade\n______\nAverage Grade\n______")
grade.grid(row=0,column=2)

grade = Label(window,bg='black',fg='white',font='Helvetica 12 bold',text="Due Date\n______\n\n______\n\n______\n\n______\n\n______")
grade.grid(row=0,column=4)


weight2 = Label(window,bg='black',fg='white',font='Helvetica 12 bold',text="Weight\n______\n15%\n______\n30%\n______\n15%\n______\n30%\n______")
weight2.grid(row=0,column=6)

lines = Label(window,bg='black',fg='white',font='Helvetica 12 bold',text="|\n|\n|\n|\n|")
lines.grid(row=0,column=1)
lines3 = Label(window,bg='black',fg='white',font='Helvetica 12 bold',text="|\n|\n|\n|\n|")
lines3.grid(row=0,column=3)
lines4 = Label(window,bg='black',fg='white',font='Helvetica 12 bold',text="|\n|\n|\n|\n|")
lines4.grid(row=0,column=5)
lines5 = Label(window,bg='black',fg='white',font='Helvetica 12 bold',text="|\n|\n|\n|\n|")
lines5.grid(row=0,column=7)



    








