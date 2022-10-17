# GUI - Graphical User Interface

# Libraries
# 1. Tkinter
# 2. PyQT
# 3. Turtle

import tkinter as ttk
app = ttk.Tk()
app.title('My App')
app.geometry('900x750')

msg = ttk.Variable(app)
print(msg.get())
msg.set("Empty")
print(msg.get())

ttk.Label(app, text = 'A simple text Label').place(x=50 , y=50)
## ttk.Label(app, text = "hello bro").place(x= 1 , y = 1)
ttk.Label(app, textvariable=msg).place(x=100, y=70)

def abc():
    print ("WoW")
    msg.set("WoW1")


ttk.Button(app, text = 'click here bro', command= abc).place(x=100, y=100)

ttk.Button(app, text = "Ye wala bhi kro bro", font = ("Arial", 16) , command = lambda:msg.set("wow1")).place(x=100, y=130)

# a func can be assigned to an identifier
# func can be taken as input argument in another func
# a func can be defined inside a python function
# a func can be returned from another func

f1 = ttk.Variable(app)
f1.set('0')
f2 = ttk.Variable(app)
f2.set('0')
result = ttk.Variable(app)

ttk.Entry(app, textvariable=f1, width = 4 , font = ('Arial', 22)).place(x=50, y=250)
ttk.Entry(app, textvariable=f2, font = ('Arial', 22)).place(x=50, y=300)
ttk.Label(app, text= "Result", font = ('Arial', 20)).place(x=50, y=550)
ttk.Label(app, textvariable=result, font=('Arial', 22)).place(x=450, y=550)

def calci(op):
    print('I will calculate')
    result.set(eval(f1.get()+op+f2.get()))


ttk.Button(app, text = '+', command = lambda:calci('+'), font =('Arial, 22')).place(x=50, y=350)
ttk.Button(app, text = '-', command = lambda:calci('-'), font =('Arial, 22')).place(x=450, y=350)
ttk.Button(app, text = '*', command = lambda:calci('*'), font =('Arial, 22')).place(x=50, y=450)
ttk.Button(app, text = '/', command = lambda:calci('/'), font =('Arial, 22')).place(x=450, y=450)

## List Box

box = ttk.Listbox(app, height=5, fg='red', activestyle='dotbox')
box.insert(1, 'Sample1')
box.insert(2, 'Sample2')
box.insert(3, 'Sample3')

box.place(x=350, y=40)

def show():
    print(box.get(box.curselection()))

ttk.Button(app, text= 'show', command=show).place(x=350, y=250)


app.mainloop()