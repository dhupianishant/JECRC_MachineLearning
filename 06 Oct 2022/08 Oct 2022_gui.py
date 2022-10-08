import tkinter
from django.db import InterfaceError


#GUI - Graphical User Interface
#Libraries
# 1. Tkinter
# 2. PyQT
# 3. Trutle

import tkinter as ttk
app = ttk.Tk()
app.title("My Application")
app.geometry("600x400") 

ttk.Label(app, text = "A Simple Text Label").place(x = 50, y = 50)
ttk.Label(app, text = "Nishant Dhupia").place(x = 50, y = 70)


app.mainloop()