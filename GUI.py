import tkinter as tk
from tkinter import ttk
def on_click():
	label1.configure(text="Te dije que no "+name.get())
	label1.configure(foreground='red')
	label1.configure(background='green')
	boton.configure(state='disable')
pass
win = tk.Tk()
win.title("Hola gui")
win.resizable(1,1)
#ttk.Label(win,text="Hola etiqueta").grid(row=0,column=0)
label1=ttk.Label(win,text="hola label")
label1.grid(row=0,column=0)
boton=ttk.Button(win,text="Dont click me",command=on_click)
boton.grid(row=1,column=1)
name=tk.StringVar()
txtEntry=ttk.Entry(win,textvariable=name)
txtEntry.grid(row=1,column=0)
#ttk.Button(win,text="click me",comman=on_click).grid(row=1,column=1)
win.mainloop()
