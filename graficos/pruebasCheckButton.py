from tkinter import *

root=Tk()

playa=IntVar()

montana=IntVar()

rural=IntVar()


root.title("Ejemplo CheckButtons")


def opciones():
	opcionEscogida=""
	if(playa.get()==1):
		opcionEscogida+=" playa"

	if(montana.get()==2):
		opcionEscogida+=" montaña"

	if(rural.get()==3):
		opcionEscogida+=" turismo rural"

	textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="avion.png")
Label(root,image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame,text="Elige destinos",width=50).pack()


Checkbutton(frame,text="Playa",variable=playa, onvalue=1, offvalue=0, command=opciones).pack()

Checkbutton(frame,text="Montaña",variable=montana, onvalue=2, offvalue=0, command=opciones).pack()

Checkbutton(frame,text="Turismo rural",variable=rural, onvalue=3, offvalue=0, command=opciones).pack()




textoFinal=Label(frame)

textoFinal.pack()

root.mainloop()