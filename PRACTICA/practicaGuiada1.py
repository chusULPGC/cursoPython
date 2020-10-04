from tkinter import *
from tkinter import messagebox
import sqlite3
from os import remove



root=Tk()

barraMenu=Menu(root)

root.config(menu=barraMenu, width=300, height=500)

miFrame=Frame(root, width=1200, height=700)
miFrame.config(bg="#F5F3F3")


miFrame.pack()



#-------------------------------------FUNCIONES---------------------------------------

def crearBBDD():
	miConexion=sqlite3.connect("Usuarios")#en el mismo comando creamos y abrimos la BBDD

	miCursor=miConexion.cursor()

	prueba=miCursor.execute('''
	CREATE TABLE DATOSUSUARIO (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_USUARIO VARCHAR(50), 	
	PASSWORD VARCHAR(50),
	APELLIDO VARCHAR(10),
	DIRECCION VARCHAR(50),
	COMENTARIOS VARCHAR(100))
	''')

	miConexion.commit()

	miConexion.close()
	messagebox.showinfo("BBDD","Base de datos creada con éxito")


def borrarBBDD():
	valor=messagebox.askokcancel("Eliminar BBDD","¿Deseas eliminar la Base de datos?") #askokcancel devuelve un valor(True,False)
	if valor==True:
		remove("Usuarios")
	messagebox.showinfo("BBDD","Base de datos eliminada con éxito")




def salirAplicacion():
	valor=messagebox.askokcancel("Salir","¿Deseas salir de la apliación?") #askokcancel devuelve un valor(True,False)
	if valor==True:
		root.destroy()


def limpiarCampos():
	miId.set("")
	miNombre.set("")
	miPass.set("")
	miApellido.set("")
	miDireccion.set("")
	textoComentario.delete(1.0,END)


def crear():	
	
	miConexion=sqlite3.connect("Usuarios")#en el mismo comando creamos y abrimos la BBDD

	miCursor=miConexion.cursor()

	nombre=cuadroNombre.get()
	password=cuadroPassword.get()
	apellido=cuadroApellido.get()
	direccion=cuadroDireccion.get()
	comentario=textoComentario.get("1.0",'end-1c')

	miCursor.execute("INSERT INTO DATOSUSUARIO (NOMBRE_USUARIO,PASSWORD,APELLIDO,DIRECCION,COMENTARIOS) VALUES(?,?,?,?,?)",(nombre,password,apellido,direccion,comentario))
	miConexion.commit()

	miConexion.close()
	messagebox.showinfo("BBDD","Datos insertados correctamente")



def leer():
	miConexion=sqlite3.connect("Usuarios")#en el mismo comando creamos y abrimos la BBDD

	miCursor=miConexion.cursor()

	identificador=cuadroId.get()
	

	miCursor.execute("SELECT * FROM DATOSUSUARIO WHERE ID=?",(identificador))
	
	personas=miCursor.fetchall()

	for persona in personas:
		name=persona[1]
		clave=persona[2]
		apellido=persona[3]
		direccion=persona[4]
		comentario=persona[5]

	miNombre.set(name)
	miPass.set(clave)
	miApellido.set(apellido)
	miDireccion.set(direccion)
	textoComentario.insert(1.0,comentario)

	miConexion.commit()

	miConexion.close()



def eliminar():

	miConexion=sqlite3.connect("Usuarios")#en el mismo comando creamos y abrimos la BBDD

	miCursor=miConexion.cursor()

	identificador=cuadroId.get()


	miCursor.execute("DELETE FROM DATOSUSUARIO WHERE ID=?",(identificador))

	miConexion.commit()

	miConexion.close()


def actualizar():

	miConexion=sqlite3.connect("Usuarios")#en el mismo comando creamos y abrimos la BBDD

	miCursor=miConexion.cursor()

	miConexion.commit()

	miConexion.close()









#-------------------------------------FIN FUNCIONES---------------------------------------







MenuBBDD=Menu(barraMenu)

#--------------------------SUBMENUS BBDD-----------------------------
MenuBBDD.add_command(label="Conectar", command=crearBBDD)

MenuBBDD.add_command(label="Borrar BBDD", command=borrarBBDD)

MenuBBDD.add_command(label="Salir",command=salirAplicacion)



#--------------------------SUBMENUS BORRAR-----------------------------
MenuBorrar=Menu(barraMenu)

MenuBorrar.add_command(label="Borrar Campos", command=limpiarCampos)

#--------------------------SUBMENUS CRUD-----------------------------
MenuCRUD=Menu(barraMenu)

MenuCRUD.add_command(label="Crear", command=crear)

MenuCRUD.add_command(label="Leer", command=leer)

MenuCRUD.add_command(label="Actualizar")

MenuCRUD.add_command(label="Borrar", command=eliminar)

#--------------------------SUBMENUS AYUDA-----------------------------

MenuAyuda=Menu(barraMenu)


MenuAyuda.add_command(label="Licencia")

MenuAyuda.add_command(label="Acerca de")




barraMenu.add_cascade(label="BBDD", menu=MenuBBDD)

barraMenu.add_cascade(label="Borrar", menu=MenuBorrar)

barraMenu.add_cascade(label="CRUD", menu=MenuCRUD)

barraMenu.add_cascade(label="Ayuda", menu=MenuAyuda)





#------------------------- ETIQUETAS(LABEL)-------------------------------------

nombreLabel=Label(miFrame,text="Id:")

nombreLabel.grid(row=0,column=0,sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame,text="Nombre:")

nombreLabel.grid(row=1,column=0,sticky="e", padx=10, pady=10)

passwordLabel=Label(miFrame,text="Contraseña:")

passwordLabel.grid(row=2,column=0,sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame,text="Apellido:")

apellidoLabel.grid(row=3,column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame,text="Dirección:")

direccionLabel.grid(row=4,column=0,sticky="e", padx=10, pady=10)

comentarioLabel=Label(miFrame,text="Comentarios:")

comentarioLabel.grid(row=5,column=0,sticky="e", padx=10, pady=10)

#------------------------- CUADROS DE TEXTO-------------------------------------
miId=StringVar()
minombre=StringVar()
miNombre=StringVar()
miPass=StringVar()
miApellido=StringVar()
miDireccion=StringVar()
miComentario=StringVar()

cuadroId=Entry(miFrame, textvariable=miId)

cuadroId.grid(row=0,column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)

cuadroNombre.grid(row=1,column=1, padx=10, pady=10)

cuadroPassword=Entry(miFrame, textvariable=miPass)

cuadroPassword.grid(row=2,column=1, padx=10, pady=10)

cuadroPassword.config(show="*")

cuadroApellido=Entry(miFrame, textvariable=miApellido)

cuadroApellido.grid(row=3,column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)

cuadroDireccion.grid(row=4,column=1)

#------------------------- AREA DE TEXTO-------------------------------------

textoComentario=Text(miFrame, width=30, height=10,borderwidth=2)

textoComentario.grid(row=5, column=1, padx=10, pady=10)


#------------------------- BOTONES -------------------------------------

botonCrear=Button(miFrame,text="Create",command=crear)

botonCrear.grid(row=6,column=0)

botonLeer=Button(miFrame,text="Read", command=leer)

botonLeer.grid(row=6,column=1)

botonActualizar=Button(miFrame,text="Update")

botonActualizar.grid(row=6,column=2)

botonBorrar=Button(miFrame,text="Delete", command=eliminar)

botonBorrar.grid(row=6,column=3,padx=10,pady=10)


root.mainloop()
