from tkinter import *
from tkinter import messagebox

root=Tk()


def infoAdicional():
	messagebox.showinfo("Procesador de Jesús","Procesador de texto versión 2020 COVID")


def avisoLicencia():
	messagebox.showwarning("Licencia","Producto bajo licencia GNU Jesús")


def salirAplicacion():
	#valor=messagebox.askquestion("Salir","¿Deseas salir de la apliación?") #askquestion devuelve un valor(yes,no)
	
	valor=messagebox.askokcancel("Salir","¿Deseas salir de la apliación?") #askokcancel devuelve un valor(True,False)
	if valor==True:
		root.destroy()


def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar","No es posible cerrar. Documento bloqueado") 
	if valor==False:
		root.destroy()


barraMenu=Menu(root)


root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu)

#--------------------------SUBMENUS ARCHIVO-----------------------------
archivoMenu.add_command(label="Nuevo")

archivoMenu.add_command(label="Guardar")

archivoMenu.add_command(label="Guardar como")

archivoMenu.add_separator()

archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)

archivoMenu.add_command(label="Salir", command=salirAplicacion)



#--------------------------SUBMENUS EDICIÓN-----------------------------
archivoEdicion=Menu(barraMenu)

archivoEdicion.add_command(label="Copiar")

archivoEdicion.add_command(label="Cortar")

archivoEdicion.add_command(label="Pegar")

#--------------------------SUBMENUS HERRAMIENTAS-----------------------------
archivoHerramientas=Menu(barraMenu)


#--------------------------SUBMENUS AYUDA-----------------------------

archivoAyuda=Menu(barraMenu)


archivoAyuda.add_command(label="Licencia", command=avisoLicencia)

archivoAyuda.add_command(label="Acerca de...",command=infoAdicional)




barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



root.mainloop()