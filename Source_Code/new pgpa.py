import tkinter as tk
window=tk.Tk()
window.title('Potential GPA Calculator')
window.geometry('500x350')
gpa=0
cla1=0
cla2=0
cla3=0
cla4=0
cla5=0
c1=0.0
c2=0.0
c3=0.0
c4=0.0
c5=0.0
c6=0.0
num1=[]
den1=[]
def calculate():
    numerator=0.0
    denominator=0.0
    if len(entbox1.get()) == 0:
        cla1=-8
    else:
        cla1=float(entbox1.get())
    if len(entbox2.get()) == 0:
        cla2=-8
    else:
        cla2=float(entbox2.get())
    if len(entbox3.get()) == 0:
        cla3=-8
    else:
        cla3=float(entbox3.get())
    if len(entbox4.get()) == 0:
        cla4=-8
    else:
        cla4=float(entbox4.get())
    if len(entbox5.get()) == 0:
        cla5=-8
    else:
        cla5=float(entbox5.get())
    if len(entbox6.get()) == 0:
        cla6=-8
    else:
        cla6=float(entbox6.get())
    if len(entbox7.get()) == 0:
        cla7=-8
    else:
        cla7=float(entbox7.get())
    if len(entbox8.get()) == 0:
        cla8=-8
    else:
        cla8=float(entbox8.get())
    if (cla1 >= 93):
        c1=4
    elif(cla1 >= 90):
        c1=3.7
    elif(cla1 >= 87):
        c1=3.3
    elif (cla1 >= 83):
        c1=3.0
    elif(cla1 >= 80):
        c1=2.7
    elif(cla1 >= 77):
        c1=2.3
    elif(cla1 >= 73):
        c1=2.0
    elif(cla1 >= 70):
        c1=1.7
    elif (cla1 >= 67):
        c1=1.3
    elif(cla1 >= 65):
        c1=1.0
    elif(cla1 < 65 and cla1>=0):
        c1=0.0
    elif(cla1 == -8):
        c8=-8

    if (cla2 >= 93):
        c2=4
    elif(cla2 >= 90):
        c2=3.7
    elif(cla2 >= 87):
        c2=3.3
    elif (cla2 >= 83):
        c2=3.0
    elif(cla2 >= 80):
        c2=2.7
    elif(cla2 >= 77):
        c2=2.3
    elif(cla2 >= 73):
        c2=2.0
    elif(cla2 >= 70):
        c2=1.7
    elif (cla2 >= 67):
        c2=1.3
    elif(cla2 >= 65):
        c2=1.0
    elif(cla2 < 65 and cla2>=0):
        c2=0.0
    elif(cla2 == -8):
        c2=-8

    if (cla3 >= 93):
        c3=4
    elif(cla3 >= 90):
        c3=3.7
    elif(cla3 >= 87):
        c3=3.3
    elif (cla3 >= 83):
        c3=3.0
    elif(cla3 >= 80):
        c3=2.7
    elif(cla3 >= 77):
        c3=2.3
    elif(cla3 >= 73):
        c3=2.0
    elif(cla3 >= 70):
        c3=1.7
    elif (cla3 >= 67):
        c3=1.3
    elif(cla3 >= 65):
        c3=1.0
    elif(cla3 < 65 and cla3>=0):
        c3=0.0
    elif(cla3 == -8):
        c3=-8

    if (cla4 >= 93):
        c4=4
    elif(cla4 >= 90):
        c4=3.7
    elif(cla4 >= 87):
        c4=3.3
    elif (cla4 >= 83):
        c4=3.0
    elif(cla4 >= 80):
        c4=2.7
    elif(cla4 >= 77):
        c4=2.3
    elif(cla4 >= 73):
        c4=2.0
    elif(cla4 >= 70):
        c4=1.7
    elif (cla4 >= 67):
        c4=1.3
    elif(cla4 >= 65):
        c4=1.0
    elif(cla4 < 65 and cla4>=0):
        c4=0.0
    elif(cla4 == -8):
        c4=-8

    if (cla5 >= 93):
        c5=4
    elif(cla5 >= 90):
        c5=3.7
    elif(cla5 >= 87):
        c5=3.3
    elif (cla5 >= 83):
        c5=3.0
    elif(cla5 >= 80):
        c5=2.7
    elif(cla5 >= 77):
        c5=2.3
    elif(cla5 >= 73):
        c5=2.0
    elif(cla5 >= 70):
        c5=1.7
    elif (cla5 >= 67):
        c5=1.3
    elif(cla5 >= 65):
        c5=1.0
    elif(cla5 < 65 and cla5>=0):
        c5=0.0
    elif(cla5 == -8):
        c5=-8

    if (cla6 >= 93):
        c6=4
    elif(cla6 >= 90):
        c6=3.7
    elif(cla6 >= 87):
        c6=3.3
    elif (cla6 >= 83):
        c6=3.0
    elif(cla6 >= 80):
        c6=2.7
    elif(cla6 >= 77):
        c6=2.3
    elif(cla6 >= 73):
        c6=2.0
    elif(cla6 >= 70):
        c6=1.7
    elif (cla6 >= 67):
        c6=1.3
    elif(cla6 >= 65):
        c6=1.0
    elif(cla6 < 65 and cla6>=0):
        c6=0.0
    elif(cla6 == -8):
        c6=-8

    if (cla7 >= 93):
        c7=4
    elif(cla7 >= 90):
        c7=3.7
    elif(cla7 >= 87):
        c7=3.3
    elif (cla7 >= 83):
        c7=3.0
    elif(cla7 >= 80):
        c7=2.7
    elif(cla7 >= 77):
        c7=2.3
    elif(cla7 >= 73):
        c7=2.0
    elif(cla7 >= 70):
        c7=1.7
    elif (cla7 >= 67):
        c7=1.3
    elif(cla7 >= 65):
        c7=1.0
    elif(cla7 < 65 and cla7>=0):
        c7=0.0
    elif(cla7 == -8):
        c7=-8

    if (cla8 >= 93):
        c8=4
    elif(cla8 >= 90):
        c8=3.7
    elif(cla8 >= 87):
        c8=3.3
    elif (cla8 >= 83):
        c8=3.0
    elif(cla8 >= 80):
        c8=2.7
    elif(cla8 >= 77):
        c8=2.3
    elif(cla8 >= 73):
        c8=2.0
    elif(cla8 >= 70):
        c8=1.7
    elif (cla8 >= 67):
        c8=1.3
    elif(cla8 >= 65):
        c8=1.0
    elif(cla8 < 65 and cla8>= 0):
        c8=0.0
    elif(cla8 == -8):
        c8=-8
    num1=[c1,c2,c3,c4,c5,c6,c7,c8]
    f = num1.count(-8)
    for i in range(f):
        num1.remove(-8)
    den1=[cla1,cla2,cla3,cla4,cla5,cla6,cla7,cla8]
    f3=den1.count(-8)
    for i in range(f3):
        den1.remove(-8)
    f2 = den1.count(-8)
    for i2 in range(f2):
        den1.remove(-8)
    for i in range(len(num1)):
        numerator+=(num1[i]*den1[i])
    for i in range(len(den1)):
        denominator+=den1[i]
    gpa=round((numerator/denominator), 2)
    gpalab1=tk.Label(window,text=gpa,fg='black',font='Helvetica 12 bold')
    gpalab1.grid(column=4,row=11,pady=45)

param=tk.Label(window,text='-8 if not appliciable',fg='black',font='Helvetica 12 bold')
param.grid(column=2,row=10)
title1=tk.Label(window,text='Class',fg='black',font='Helvetica 12 bold')
title1.grid(column=1,row=1)
cl1=tk.Label(window,text='Class 1',fg='black',font='Helvetica 12 bold')
cl1.grid(column=1,row=2)
cl2=tk.Label(window,text='Class 2',fg='black',font='Helvetica 12 bold')
cl2.grid(column=1,row=3)
cl3=tk.Label(window,text='Class 3',fg='black',font='Helvetica 12 bold')
cl3.grid(column=1,row=4)
cl4=tk.Label(window,text='Class 4',fg='black',font='Helvetica 12 bold')
cl4.grid(column=1,row=5)
cl5=tk.Label(window,text='Class 5',fg='black',font='Helvetica 12 bold')
cl5.grid(column=1,row=6)
cl6=tk.Label(window,text='Class 6',fg='black',font='Helvetica 12 bold')
cl6.grid(column=1,row=7)
cl7=tk.Label(window,text='Class 7',fg='black',font='Helvetica 12 bold')
cl7.grid(column=1,row=8)
cl8=tk.Label(window,text='Class 8',fg='black',font='Helvetica 12 bold')
cl8.grid(column=1,row=9)
grade=tk.Label(window,text='Grade',fg='black',font='Helvetica 12 bold')
grade.grid(column=2,row=1)
credit=tk.Label(window,text='Credits',fg='black',font='Helvetica 12 bold')
credit.grid(column=3,row=1)
gpalab=tk.Label(window,text="Potential Gpa:",fg='black',font='Helvetica 12 bold')
gpalab.grid(column=3,row=11,pady=45)


entbox1=tk.Entry(window,bg='grey')
entbox1.grid(row=2,column=2)

entbox2=tk.Entry(window,bg='grey')
entbox2.grid(row=3,column=2)

entbox3=tk.Entry(window,bg='grey')
entbox3.grid(row=4,column=2)

entbox4=tk.Entry(window,bg='grey')
entbox4.grid(row=5,column=2)

entbox5=tk.Entry(window,bg='grey')
entbox5.grid(row=6,column=2)

entbox6=tk.Entry(window,bg='grey')
entbox6.grid(row=7,column=2)

entbox7=tk.Entry(window,bg='grey')
entbox7.grid(row=8,column=2)

entbox8=tk.Entry(window,bg='grey')
entbox8.grid(row=9,column=2)


entbox1c=tk.Entry(window,bg='grey')
entbox1c.grid(row=2,column=3)

entbox2c=tk.Entry(window,bg='grey')
entbox2c.grid(row=3,column=3)

entbox3c=tk.Entry(window,bg='grey')
entbox3c.grid(row=4,column=3)

entbox4c=tk.Entry(window,bg='grey')
entbox4c.grid(row=5,column=3)

entbox5c=tk.Entry(window,bg='grey')
entbox5c.grid(row=6,column=3)

entbox6c=tk.Entry(window,bg='grey')
entbox6c.grid(row=7,column=3)

entbox7c=tk.Entry(window,bg='grey')
entbox7c.grid(row=8,column=3)

entbox8c=tk.Entry(window,bg='grey')
entbox8c.grid(row=9,column=3)



continue1=tk.Button(window,bg='grey',text='Calculate',font='Helvetica 12 bold',command=calculate)
continue1.grid(column=0,row=11,pady=45)



window.mainloop()



