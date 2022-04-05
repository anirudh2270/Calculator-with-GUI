from tkinter import*

root = Tk()
root.title ("Calculator")
root.resizable(0,0)
e = Entry(root,width= 60,borderwidth=2,font=("arial",10,"bold"))
e.grid(row=0,column=0,columnspan=4,pady=10)

def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0, END)

def button_addition():
    first = e.get()
    global f_num
    f_num = int(first)
    global maths
    maths = "Add"
    e.delete(0, END)

def button_multiply():
    first = e.get()
    global f_num
    f_num = int(first)
    global maths
    maths = "multiply"
    e.delete(0, END)

def button_divide():
    first = e.get()
    global f_num
    f_num = int(first)
    global maths
    maths = "divide"
    e.delete(0, END)

def button_subtract():
    first = e.get()
    global f_num
    f_num = int(first)
    global maths
    maths = "subtract"
    e.delete(0, END)

def button_equal():
    s = e.get()
    e.delete(0, END)
    if maths == "subtract":
     e.insert(0, f_num - int(s))

    if maths == "divide":
     e.insert(0, f_num / int(s))

    if maths == "Add":
     e.insert(0, f_num + int(s))

    if maths == "multiply":
     e.insert(0, f_num * int(s))
    

    

b1 = Button(root,text="1",padx=40,pady=20,command=lambda:button_add(1),borderwidth=1)
b2 = Button(root,text="2",padx=40,pady=20,command=lambda:button_add(2),borderwidth=1)
b3 = Button(root,text="3",padx=40,pady=20,command=lambda:button_add(3),borderwidth=1)
b4 = Button(root,text="4",padx=40,pady=20,command=lambda:button_add(4),borderwidth=1)
b5 = Button(root,text="5",padx=40,pady=20,command=lambda:button_add(5),borderwidth=1)
b6 = Button(root,text="6",padx=40,pady=20,command=lambda:button_add(6),borderwidth=1)
b7 = Button(root,text="7",padx=40,pady=20,command=lambda:button_add(7),borderwidth=1)
b8 = Button(root,text="8",padx=40,pady=20,command=lambda:button_add(8),borderwidth=1)
b9 = Button(root,text="9",padx=40,pady=20,command=lambda:button_add(9),borderwidth=1)
b10 = Button(root,text="0",padx=90,pady=20,command=lambda:button_add(0),borderwidth=1)
b11 = Button(root,text= ".",padx=40,pady=20,command=lambda:button_add("."),borderwidth=1)
b12 = Button(root,text= "=",padx=90,pady=20,command=button_equal,borderwidth=1)
b13 = Button(root,text= "C",padx=40,pady=20,command=button_clear,borderwidth=1)
b14 = Button(root,text= "+",padx=40,pady=20,command=button_addition,borderwidth=1)
b15 = Button(root,text= "-",padx=40,pady=20,command=button_subtract,borderwidth=1)
b16 = Button(root,text= "*",padx=40,pady=20,command=button_multiply,borderwidth=1)
b17 = Button(root,text= "/",padx=40,pady=20,command=button_divide,borderwidth=1)


b7.grid(row=1,column=0,sticky=NSEW)
b8.grid(row=1,column=1,sticky=NSEW)
b9.grid(row=1,column=2,sticky=NSEW)

b4.grid(row=2,column=0,sticky=NSEW)
b5.grid(row=2,column=1,sticky=NSEW)
b6.grid(row=2,column=2,sticky=NSEW)


b1.grid(row=3,column=0,sticky=NSEW)
b2.grid(row=3,column=1,sticky=NSEW)
b3.grid(row=3,column=2,sticky=NSEW)

b10.grid(row=4,column=0,columnspan=2,sticky=NSEW)
b11.grid(row=4,column=2,sticky=NSEW)
b12.grid(row=5,column=0,columnspan=2,sticky=NSEW)
b13.grid(row=5,column=2,columnspan=2,sticky=NSEW)
b14.grid(row=1,column=3,sticky=NSEW)
b15.grid(row=2,column=3,sticky=NSEW)
b16.grid(row=3,column=3,sticky=NSEW)
b17.grid(row=4,column=3,sticky=NSEW)






root.mainloop()