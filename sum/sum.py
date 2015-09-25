from Tkinter import *
import ttk

root = Tk()

root.title('Sum of two numbers')
root.geometry('250x150+300+300')

mainframe = ttk.Frame(root, padding='12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

a = StringVar()
ttk.Label(mainframe, text='Number a: ', padding='3').grid(column=1, row=1, sticky=E)
a_entry = ttk.Entry(mainframe, width=10, textvariable=a)
a_entry.grid(column=2, row=1, sticky=(W, E))

b = StringVar()
ttk.Label(mainframe, text='Number b: ', padding='3').grid(column=1, row=2, sticky=E)
b_entry = ttk.Entry(mainframe, width=10,textvariable=b)
b_entry.grid(column=2, row=2, sticky =(W,E))

sum = StringVar()
ttk.Label(mainframe, text='Sum is = ', padding='3').grid(column=1, row=3, sticky=E)

def sum(a, b):
    try:
        a.set(float(a.get()))
        b.set(float(b.get()))
        sum.set(a+b)
    except ValueError:
        pass

root.mainloop()