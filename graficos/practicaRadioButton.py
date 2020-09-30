from tkinter import *

root=Tk()

opciones=IntVar()

#rescatamos los valores pulsados para saber que boton esta seleccionado

def imprimir():
	#print(opciones.get())
	if(opciones.get()==1):
		etiqueta.config(text="Has elegido Masculino")
	else:
		etiqueta.config(text="Has elegido Femenino")


Label(root, text="Genero:").pack()

Radiobutton(root,text="Masculino",variable=opciones, value=1, command=imprimir).pack()

Radiobutton(root,text="Femenino",variable=opciones, value=2, command=imprimir).pack()



etiqueta=Label(root)
etiqueta.pack()

root.mainloop()