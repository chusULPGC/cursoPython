from tkinter import *

raiz=Tk()


miFrame=Frame(raiz, width=1200, height=600)
miFrame.config(bg="#F5F3F3")


miFrame.pack()

#------------------------- ETIQUETAS(LABEL)-------------------------------------

nombreLabel=Label(miFrame,text="Nombre:")

nombreLabel.grid(row=0,column=0,sticky="e", padx=10, pady=10)

passwordLabel=Label(miFrame,text="Contraseña:")

passwordLabel.grid(row=1,column=0,sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame,text="Apellido:")

apellidoLabel.grid(row=2,column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame,text="Dirección:")

direccionLabel.grid(row=3,column=0,sticky="e", padx=10, pady=10)

comentarioLabel=Label(miFrame,text="Comentarios:")

comentarioLabel.grid(row=4,column=0,sticky="e", padx=10, pady=10)

#------------------------- CUADROS DE TEXTO-------------------------------------

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)

cuadroNombre.grid(row=0,column=1, padx=10, pady=10)
cuadroNombre.config(fg="blue",bg="yellow")

cuadroPassword=Entry(miFrame)

cuadroPassword.grid(row=1,column=1, padx=10, pady=10)

cuadroPassword.config(show="*")

cuadroApellido=Entry(miFrame)

cuadroApellido.grid(row=2,column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)

cuadroDireccion.grid(row=3,column=1)

#------------------------- AREA DE TEXTO-------------------------------------

textoComentario=Text(miFrame, width=30, height=10,borderwidth=2)

textoComentario.grid(row=4, column=1, padx=10, pady=10)

#------------------------- AÑADIMOS BARRA DE SCROLL AL CUADRO DE TEXTO -------------------------------------

scrollVertical=Scrollbar(miFrame,command=textoComentario.yview)

scrollVertical.grid(row=4, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVertical.set)


#------------------------- BOTONES-------------------------------------

def codigoBoton():
	minombre.set("Chus")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)

botonEnvio.pack()




raiz.mainloop()



















