import serial
import tkinter as tk
from tkinter import ttk
puerto= serial.Serial('/dev/ttyACM0',9600,timeout=1)
def on_prender():
	global puerto
	puerto.write("a".encode())
pass
def on_apagar():
	global puerto
	puerto.write("z".encode())
win = tk.Tk()
win.title("Encender y apagar")
win.resizable(0,0)
boton=ttk.Button(win,text="apagar",command=on_apagar)
boton.grid(row=1,column=1)
boton=ttk.Button(win,text="prender",command=on_prender)
boton.grid(row=1,column=3)
win.mainloop()
