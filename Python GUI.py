from tkinter import *

window=Tk()
window.title('Class Manager')
window.geometry('600x300')
window.configure(bg='black')

assignment = Label(window,bg='black',fg='blue',font='Helvetica 12 bold', text="Assignment Type")
class1 = Label(window,bg='black',fg='white', text="Homework")
class2 = Label(window,bg='black',fg='white', text="Tests")
class3 = Label(window,bg='black',fg='white', text="Quizzes")
class4 = Label(window,bg='black',fg='white', text="Project")
grade = Label(window,bg='black',fg='blue',font='Helvetica 12 bold',text="Grade")
grade1= Label(window,bg='black',fg='white', text="Average Grade")
grade2= Label(window,bg='black',fg='white', text="Average Grade")
grade3= Label(window,bg='black',fg='white', text="Average Grade")
grade4= Label(window,bg='black',fg='white', text="Average Grade")
weight1 = Label(window,bg='black',fg='blue',font='Helvetica 12 bold',text="Weight")
weight2 = Label(window,bg='black',fg='white',text="15%")
weight3 = Label(window,bg='black',fg='white',text="30%")
weight4 = Label(window,bg='black',fg='white',text="15%")
weight5 = Label(window,bg='black',fg='white',text="30%")
duedate= Label(window,bg='black',fg='blue',font='Helvetica 12 bold',text="Due Date")
line0 = Label(window,bg='black',fg='white', text="________")
line1 = Label(window,bg='black',fg='white', text="________")
line2 = Label(window,bg='black',fg='white', text="________")
line3 = Label(window,bg='black',fg='white', text="________")
line4 = Label(window,bg='black',fg='white', text="________")
line5 = Label(window,bg='black',fg='white', text="________")
line6 = Label(window,bg='black',fg='white', text="________")
line7 = Label(window,bg='black',fg='white', text="________")
line8 = Label(window,bg='black',fg='white', text="________")
line9 = Label(window,bg='black',fg='white', text="________")
line10 = Label(window,bg='black',fg='white', text="________")
line11 = Label(window,bg='black',fg='white', text="________")
line12 = Label(window,bg='black',fg='white', text="________")
line13 = Label(window,bg='black',fg='white', text="________")
line14 = Label(window,bg='black',fg='white', text="________")
line15 = Label(window,bg='black',fg='white', text="________")
line16 = Label(window,bg='black',fg='white', text="________")
line17 = Label(window,bg='black',fg='white', text="________")
line18 = Label(window,bg='black',fg='white', text="________")
line19 = Label(window,bg='black',fg='white', text="________")
line20 = Label(window,bg='black',fg='white', text="________")
line21 = Label(window,bg='black',fg='white', text="________")
line22 = Label(window,bg='black',fg='white', text="________")
line23 = Label(window,bg='black',fg='white', text="________")
line0 = Label(window,bg='black',fg='white', text="________")
midline0 = Label(window,bg='black',fg='white',text="|")
midline1 = Label(window,bg='black',fg='white',text="|")
midline2 = Label(window,bg='black',fg='white',text="|")
midline3 = Label(window,bg='black',fg='white',text="|")
midline4 = Label(window,bg='black',fg='white',text="|")
midline5 = Label(window,bg='black',fg='white',text="|")
midline6 = Label(window,bg='black',fg='white',text="|")
midline7 = Label(window,bg='black',fg='white',text="|")
midline8 = Label(window,bg='black',fg='white',text="|")
midline9 = Label(window,bg='black',fg='white',text="|")
midline10 = Label(window,bg='black',fg='white',text="|")
midline11 = Label(window,bg='black',fg='white',text="|")
midline12 = Label(window,bg='black',fg='white',text="|")
midline13 = Label(window,bg='black',fg='white',text="|")
midline14 = Label(window,bg='black',fg='white',text="|")
midline15 = Label(window,bg='black',fg='white',text="|")
midline16 = Label(window,bg='black',fg='white',text="|")
midline17 = Label(window,bg='black',fg='white',text="|")
midline18 = Label(window,bg='black',fg='white',text="|")
midline19 = Label(window,bg='black',fg='white',text="|")
midline20 = Label(window,bg='black',fg='white',text="|")
midline21 = Label(window,bg='black',fg='white',text="|")
midline22 = Label(window,bg='black',fg='white',text="|")
midline23 = Label(window,bg='black',fg='white',text="|")
midline24 = Label(window,bg='black',fg='white',text="|")
midline25 = Label(window,bg='black',fg='white',text="|")
midline26 = Label(window,bg='black',fg='white',text="|")
midline27 = Label(window,bg='black',fg='white',text="|")
midline28 = Label(window,bg='black',fg='white',text="|")
midline29 = Label(window,bg='black',fg='white',text="|")
midline30 = Label(window,bg='black',fg='white',text="|")
midline31 = Label(window,bg='black',fg='white',text="|")
midline32 = Label(window,bg='black',fg='white',text="|")
midline33 = Label(window,bg='black',fg='white',text="|")
midline34 = Label(window,bg='black',fg='white',text="|")
midline35 = Label(window,bg='black',fg='white',text="|")
midline36 = Label(window,bg='black',fg='white',text="|")
midline37 = Label(window,bg='black',fg='white',text="|")
midline38 = Label(window,bg='black',fg='white',text="|")
midline39 = Label(window,bg='black',fg='white',text="|")
midline40 = Label(window,bg='black',fg='white',text="|")


line9.grid(row=2,column=2)
grade.grid(row=1,column=2)
midline0.grid(row=1,column=1)
midline1.grid(row=2,column=1)
midline2.grid(row=3,column=1)
midline3.grid(row=4,column=1)
midline4.grid(row=5,column=1)
midline5.grid(row=6,column=1)
midline6.grid(row=7,column=1)
midline7.grid(row=8,column=1)
midline8.grid(row=9,column=1)
midline9.grid(row=10,column=1)
assignment.grid(row=1,column=0)
line0.grid(row=2,column=0)
class1.grid(row=3,column=0)
#
line1.grid(row=4,column=0)
#
class2.grid(row=5,column=0)
#
line2.grid(row=6,column=0)
#
class3.grid(row=7,column=0)
#
line3.grid(row=8,column=0)
#
class4.grid(row=9,column=0)
#
line4.grid(row=10,column=0)
#

grade1.grid(row=3,column=2)
line5.grid(row=4,column=2)
grade2.grid(row=5,column=2)
line6.grid(row=6,column=2)
grade3.grid(row=7,column=2)
line7.grid(row=8,column=2)
grade4.grid(row=9,column=2)
line8.grid(row=10,column=2)


midline10.grid(row=1,column=4)
midline11.grid(row=2,column=4)
midline12.grid(row=3,column=4)
midline13.grid(row=4,column=4)
midline14.grid(row=5,column=4)
midline15.grid(row=6,column=4)
midline16.grid(row=7,column=4)
midline17.grid(row=8,column=4)
midline18.grid(row=9,column=4)
midline19.grid(row=10,column=4)
midline21.grid(row=1,column=6)
midline22.grid(row=2,column=6)
midline23.grid(row=3,column=6)
midline24.grid(row=4,column=6)
midline25.grid(row=5,column=6)
midline26.grid(row=6,column=6)
midline27.grid(row=7,column=6)
midline28.grid(row=8,column=6)
midline29.grid(row=9,column=6)
midline30.grid(row=10,column=6)



weight1.grid(row=1,column=5)
line10.grid(row=2,column=5)
weight2.grid(row=3,column=5)
line11.grid(row=4,column=5)
weight3.grid(row=5,column=5)
line12.grid(row=6,column=5)
weight4.grid(row=7,column=5)
line13.grid(row=8,column=5)
weight5.grid(row=9,column=5)
line14.grid(row=10,column=5)

duedate.grid(row=1,column=7)
line15.grid(row=2,column=7)
line16.grid(row=3,column=7)
line17.grid(row=4,column=7)
line18.grid(row=5,column=7)
line19.grid(row=6,column=7)
line20.grid(row=7,column=7)
line21.grid(row=8,column=7)
line22.grid(row=9,column=7)
line23.grid(row=10,column=7)
midline31.grid(row=1,column=8)
midline32.grid(row=2,column=8)
midline33.grid(row=3,column=8)
midline34.grid(row=4,column=8)
midline35.grid(row=5,column=8)
midline36.grid(row=6,column=8)
midline37.grid(row=7,column=8)
midline38.grid(row=8,column=8)
midline39.grid(row=9,column=8)
midline40.grid(row=10,column=8)















