import tkinter as tk
from tkinter import ttk
def on_buttonclick():
	textoActual=Label2text.get()
	Label2text.set(textoActual+"1")
pass

def on_button2click():
	textoActual=Label2text.get()
	Label2text.set(textoActual+"2")
pass

def on_button3click():
        textoActual=Label2text.get()
        Label2text.set(textoActual+"3")
pass

def on_button4click():
        textoActual=Label2text.get()
        Label2text.set(textoActual+"4")
pass

def on_button5click():
        textoActual=Label2text.get()
        Label2text.set(textoActual+"5")
pass

def on_button6click():
        textoActual=Label2text.get()
        Label2text.set(textoActual+"6")
pass

def on_button7click():
        textoActual=Label2text.get()
        Label2text.set(textoActual+"7")
pass

def on_button8click():
        textoActual=Label2text.get()
        Label2text.set(textoActual+"8")
pass

def on_button9click():
        textoActual=Label2text.get()
        Label2text.set(textoActual+"9")
pass

def on_button0click():
        textoActual=Label2text.get()
        Label2text.set(textoActual+"0")
pass

def on_button10click():
        textoActual=Label2text.get()
        Label2text.set(textoActual+".")
pass

def on_button11click():
        textoActual=Label2text.get()
        Label2text.set("")
pass

def on_suma():
	global operacion
	global textoActual
	textoActual=Label2text.get()
	operacion='+'
	Label2text.set("")

	#if(operacion==)
		#Label2text=textoActual+Label2text
		#operacion=
pass

def on_resta():
	global operacion
	global textoActual
	textoActual=Label2text.get()
	operacion='-'
	Label2text.set("")
pass

def on_multiplicacion():
        global operacion
        global textoActual
        textoActual=Label2text.get()
        operacion='X'
        Label2text.set("")
pass

def on_division():
        global operacion
        global textoActual
        textoActual=Label2text.get()
        operacion='/'
        Label2text.set("")
pass

def on_igual():
	global operacion
	if(operacion=='+'):
		Label2text.set(str(float(textoActual)+float(Label2text.get())))
		operacion1=operacion
	elif(operacion=='-'):
		Label2text.set(str(float(textoActual)-float(Label2text.get())))
		operacion1=operacion
	elif(operacion=='X'):
                Label2text.set(str(float(textoActual)*float(Label2text.get())))
                operacion1=operacion
	elif(operacion=='/'):
                Label2text.set(str(float(textoActual)/float(Label2text.get())))
                operacion1=operacion
pass

operacion=''
textoActual=''
win=tk.Tk()
win.title("Calculadora")
win.resizable(1,1)
label1=ttk.Label(win,text="Calculadora")
label1.grid(row=1,column=2)
boton=ttk.Button(win,text="1",command=on_buttonclick)
boton.grid(row=4,column=0)
boton2=ttk.Button(win,text="2",command=on_button2click)
boton2.grid(row=4,column=1)
boton3=ttk.Button(win,text="3",command=on_button3click)
boton3.grid(row=4,column=2)
boton4=ttk.Button(win,text="4",command=on_button4click)
boton4.grid(row=5,column=0)
boton5=ttk.Button(win,text="5",command=on_button5click)
boton5.grid(row=5,column=1)
boton6=ttk.Button(win,text="6",command=on_button6click)
boton6.grid(row=5,column=2)
boton7=ttk.Button(win,text="7",command=on_button7click)
boton7.grid(row=6,column=0)
boton8=ttk.Button(win,text="8",command=on_button8click)
boton8.grid(row=6,column=1)
boton9=ttk.Button(win,text="9",command=on_button9click)
boton9.grid(row=6,column=2)
boton10=ttk.Button(win,text="0",command=on_button0click)
boton10.grid(row=7,column=1)
boton11=ttk.Button(win,text=".",command=on_button10click)
boton11.grid(row=7,column=2)
boton12=ttk.Button(win,text="/",command=on_division)
boton12.grid(row=4,column=3)
boton13=ttk.Button(win,text="X",command=on_multiplicacion)
boton13.grid(row=5,column=3)
boton14=ttk.Button(win,text="-",command=on_resta)
boton14.grid(row=6,column=3)
boton14=ttk.Button(win,text="+",command=on_suma)
boton14.grid(row=7,column=3)
boton15=ttk.Button(win,text="=",command=on_igual)
boton15.grid(row=8,column=3)
boton16=ttk.Button(win,text="CE",command=on_button11click)
boton16.grid(row=7,column=0)
Label2text=tk.StringVar()
label2=ttk.Label()
label2.configure(textvar=Label2text)
label2.grid(row=2,column=3)

win.mainloop()
