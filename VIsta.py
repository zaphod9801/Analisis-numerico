from tkinter import *    
from tkinter import ttk, font
from Metodos import *

App = Tk()
App.configure(bg = 'beige')
App.title('Análisis numérico')

fuente = font.Font(weight='bold')

f = ttk.Label(App, text="función:", font=fuente).pack(fill= BOTH)
n = ""

t = ttk.Entry(App, textvariable=n, width=30).pack(fill= BOTH)

ttk.Button(App, text='Salir', command=quit).pack(side=BOTTOM)

App.mainloop()