import tkinter as tk
window=tk.Tk()
window.title('Potential GPA Calculator')
window.geometry('350x200')



title1=tk.Label(window,text='Class',fg='black')
title1.grid(column=1,row=1)
title2=tk.Label(window,text='Class 1',fg='black')
title2.grid(column=1,row=2)
title3=tk.Label(window,text='Class 2',fg='black')
title3.grid(column=1,row=3)
title4=tk.Label(window,text='Class 3',fg='black')
title4.grid(column=1,row=4)
title5=tk.Label(window,text='Class 4',fg='black')
title5.grid(column=1,row=5)
title1a=tk.Label(window,text='Grade',fg='black')
title1a.grid(column=2,row=1)
gpalab=tk.Label(window,text="Potential Gpa:",fg='black')
gpalab.grid(column=3,row=6,pady=50)


entbox3=tk.Entry(window,bg='grey')
entbox3.grid(row=4,column=2)

entbox3=tk.Entry(window,bg='grey')
entbox3.grid(row=5,column=2)

entbox2=tk.Entry(window,bg='grey')
entbox2.grid(row=2,column=2)

entbox3=tk.Entry(window,bg='grey')
entbox3.grid(row=3,column=2)



continue1=tk.Button(window,bg='grey',text='Calculate')
continue1.grid(column=0,row=6,pady=50)


window.mainloop()



