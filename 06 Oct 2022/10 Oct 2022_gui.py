import tkinter as ttk
app =ttk.Tk()

app.title("Movie Recommender")
app.geometry("900x600")

result = ttk.Variable(app)

box = ttk.Listbox(app, height = 10, fg = 'red', activestyle = 'dotbox')
box.insert(1, 'Sample1')
box.insert(2, 'Sample2')
box.insert(3, 'Sample3')
box.place(x = 10, y = 10)

def getMovie():
    pass

ttk.Button(app, text = 'Find Recommendation', command = getMovie).place(x = 300, y = 10)
ttk.Label(app, textvariable = result).place(x = 300, y = 100)

app.mainloop()