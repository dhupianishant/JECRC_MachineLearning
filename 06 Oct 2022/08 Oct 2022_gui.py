# Importing the Modules
from email import message
import tkinter
from django.db import InterfaceError


# GUI - Graphical User Interface
# Libraries
# 1. Tkinter
# 2. PyQT
# 3. Trutle

# Importing the Modules
import tkinter as ttk

# Starting the App and giving it Title and Geometry
app = ttk.Tk()
app.title("My Application")
app.geometry("600x400") 

message = ttk.Variable(app)

# Text Labels
ttk.Label(app, text = "A Simple Text Label").place(x = 50, y = 50)
ttk.Label(app, textvariable=message).place(x = 50, y = 70)

#Defining a Function
def abc():
    print("Wow")
    message.set("Jo tera man kre")

# Button
ttk.Button(app, text = "Isko Click Kardo", command = abc).place(x = 100, y = 100)
ttk.Button(app, text = "Isko bhi", command = lambda: message.set("Pata Nhi")).place(x = 100, y = 130)

f1 = ttk.Variable(app)
f1.set('0')
f2 = ttk.Variable(app)
f2.set('0')
result = ttk.Variable(app)
ttk.Entry(app, textvariable=f1, font = ('Arial', 22), width=4).place(x=50, y=200)
ttk.Entry(app, textvariable=f2, font = ('Arial', 22), width=4).place(x=50, y=250)

def cal(op):
    print("I will calculate")
    result.set(eval(f1.get()+op+f2.get()))

ttk.Button(app, text='+', command = lambda: cal('+'), font = ("Arial", 22)).place(x=50, y=350)
ttk.Button(app, text='-', command = lambda: cal('-'), font = ("Arial", 22)).place(x=450, y=350)
ttk.Button(app, text='*', command = lambda: cal('*'), font = ("Arial", 22)).place(x=50, y=450)
ttk.Button(app, text='/', command = lambda: cal('/'), font = ("Arial", 22)).place(x=450, y=450)

ttk.Label(app, text = 'Result will be declared soon.').place(x=50, y=550)
ttk.Label(app, textvariable = result, font=("Arial", 22)).place(x=450, y=550)

box = ttk.Listbox(app, fg='red', activestyle='dotbox')
box.insert('1', 'Sample1')
box.insert('2', 'Sample2')
box.insert('3', 'Sample3')
box.place(x=1000, y=450)

def show():
    print(box.get(box.curselection()))

# Main Command, always stays at the bottom
app.mainloop()