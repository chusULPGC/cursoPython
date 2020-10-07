from tkinter import *
from tkinter import messagebox
import sqlite3
from os import remove



root=Tk()
root.config(bg="#9DC3DB")
root.resizable(0,0)# con esto evito que se pueda agrandar el tamaño de la ventana

barraMenu=Menu(root)

root.config(menu=barraMenu, width=300, height=300)

miFrame=Frame(root)
miFrame.config(bg="#9DC3DB")



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
	limpiarCampos()




def leer():
	miConexion=sqlite3.connect("Usuarios")#en el mismo comando creamos y abrimos la BBDD

	miCursor=miConexion.cursor()

	identificador=cuadroId.get()
	print(identificador)

	miCursor.execute("SELECT * FROM DATOSUSUARIO WHERE ID=?", identificador)
	limpiarCampos()

	
	personas=miCursor.fetchall()

	for persona in personas:
		ident=persona[0]
		name=persona[1]
		clave=persona[2]
		apellido=persona[3]
		direccion=persona[4]
		comentario=persona[5]

	miId.set(ident)
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



	valor=messagebox.askokcancel("Eliminar campo","¿Deseas eliminar el campo de la Base de datos?") #askokcancel devuelve un valor(True,False)

	if valor==True:
	
		miCursor.execute("DELETE FROM DATOSUSUARIO WHERE ID=?",(identificador,))

		miConexion.commit()

		miConexion.close()
		messagebox.showinfo("BBDD","Campo eliminado correctamente")



def actualizar():

	miConexion=sqlite3.connect("Usuarios")#en el mismo comando creamos y abrimos la BBDD

	miCursor=miConexion.cursor()

	identificador=cuadroId.get()
	nombre=cuadroNombre.get()
	password=cuadroPassword.get()
	apellido=cuadroApellido.get()
	direccion=cuadroDireccion.get()
	comentario=textoComentario.get("1.0",'end-1c')

	miCursor.execute("UPDATE DATOSUSUARIO SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? WHERE ID=?",(nombre,password,apellido,direccion,comentario,identificador))


	miConexion.commit()

	miConexion.close()
	messagebox.showinfo("BBDD","Datos actualizados correctamente")
	limpiarCampos()




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

MenuCRUD.add_command(label="Actualizar", command=actualizar)

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

idLabel=Label(miFrame,text="Id: ")

idLabel.grid(row=0,column=0,sticky="w", padx=10, pady=10)
idLabel.config(bg="#9DC3DB")

nombreLabel=Label(miFrame,text="Nombre: ")

nombreLabel.grid(row=1,column=0,sticky="w", padx=10, pady=10)
nombreLabel.config(bg="#9DC3DB")

passwordLabel=Label(miFrame,text="Contraseña: ")

passwordLabel.grid(row=2,column=0,sticky="w", padx=10, pady=10)
passwordLabel.config(bg="#9DC3DB")

apellidoLabel=Label(miFrame,text="Apellido: ")

apellidoLabel.grid(row=3,column=0, sticky="w", padx=10, pady=10)
apellidoLabel.config(bg="#9DC3DB")

direccionLabel=Label(miFrame,text="Dirección: ")

direccionLabel.grid(row=4,column=0,sticky="w", padx=10, pady=10)
direccionLabel.config(bg="#9DC3DB")

comentarioLabel=Label(miFrame,text="Comentarios: ")

comentarioLabel.grid(row=5,column=0,sticky="w", padx=10, pady=10)
comentarioLabel.config(bg="#9DC3DB")

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
cuadroId.configure(font=("Courier", 16, "italic"))

cuadroNombre=Entry(miFrame, textvariable=miNombre)

cuadroNombre.grid(row=1,column=1, padx=10, pady=10)
cuadroNombre.configure(font=("Courier", 16, "italic"))

cuadroPassword=Entry(miFrame, textvariable=miPass)

cuadroPassword.grid(row=2,column=1, padx=10, pady=10)
cuadroPassword.configure(font=("Courier", 16, "italic"))

cuadroPassword.config(show="*")

cuadroApellido=Entry(miFrame, textvariable=miApellido)

cuadroApellido.grid(row=3,column=1, padx=10, pady=10)
cuadroApellido.configure(font=("Courier", 16, "italic"))

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)

cuadroDireccion.grid(row=4,column=1, padx=10, pady=10)
cuadroDireccion.configure(font=("Courier", 16, "italic"))

#------------------------- AREA DE TEXTO-------------------------------------

textoComentario=Text(miFrame, width=20, height=10,borderwidth=2)

textoComentario.grid(row=5, column=1, padx=10, pady=10)
textoComentario.configure(font=("Courier", 16, "italic"))


#------------------------- BOTONES -------------------------------------

miFrame2=Frame(root)
miFrame2.config(bg="#6966F7")
miFrame2.pack()

botonCrear=Button(miFrame2,text="Crear",command=crear)

botonCrear.grid(row=1,column=0, sticky="e", padx=20, pady=10)

botonLeer=Button(miFrame2,text="Leer", command=leer)

botonLeer.grid(row=1,column=1, sticky="e", padx=20, pady=10)

botonActualizar=Button(miFrame2,text="Actualizar", command=actualizar)

botonActualizar.grid(row=1,column=2, sticky="e", padx=20, pady=10)

botonBorrar=Button(miFrame2,text="Eliminar", command=eliminar)

botonBorrar.grid(row=1,column=3, sticky="e", padx=20, pady=10)
root.mainloop()
