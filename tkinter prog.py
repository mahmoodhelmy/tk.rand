from tkinter import *
from random import randint
root = Tk()
win= root.geometry('300x300')
F_label = Label(root,text="First Program")
F_label.grid(column=0,row=0,padx=20)
e=Entry(root,textvariable=IntVar())
e.grid(row=1,column=1)


e2=Entry(root,textvariable=IntVar())
e2.grid(row=2,column=1)


def en():
    x =int(e.get())
    y =int(e2.get())
    e.delete(0,END)
    e.insert(0,x)
    e2.delete(0,END)
    e2.insert(0,y)
    zp= randint(x,y)
    sl=Label(root,text=zp, textvariable=StringVar)
    sl.grid(column=10,row=10)
    return zp
    
b=Button(root,command=en,text='res')
b.grid(row=5,column=5)
print('+')
root.mainloop()