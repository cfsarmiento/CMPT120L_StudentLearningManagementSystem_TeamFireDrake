import tkinter as tk
window=tk.Tk()
window.title('Login Setup')
window.geometry('300x150')



title1=tk.Label(window,text='Set Username',fg='black')
title1.grid(column=1,row=1)
title2=tk.Label(window,text='Set Password',fg='black')
title2.grid(column=1,row=2)
title3=tk.Label(window,text='Confirm Password',fg='black')
title3.grid(column=1,row=3)


entbox1=tk.Entry(window,bg='grey')
entbox1.grid(row=1,column=2)

entbox2=tk.Entry(window,bg='grey')
entbox2.grid(row=2,column=2)

entbox3=tk.Entry(window,bg='grey')
entbox3.grid(row=3,column=2)



continue1=tk.Button(window,bg='grey',text='Continue')
continue1.grid(column=3,row=4,pady=50)


window.mainloop()



