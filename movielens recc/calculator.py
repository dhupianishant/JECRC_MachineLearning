import tkinter as ttk
app = ttk.Tk()
app.title('My App')
app.geometry('900x750')



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


app.mainloop()