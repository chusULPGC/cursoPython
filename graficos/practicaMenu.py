from tkinter import *


root=Tk()

barraMenu=Menu(root)


root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu)

#--------------------------SUBMENUS ARCHIVO-----------------------------
archivoMenu.add_command(label="Nuevo")

archivoMenu.add_command(label="Guardar")

archivoMenu.add_command(label="Guardar como")

archivoMenu.add_separator()

archivoMenu.add_command(label="Cerrar")

archivoMenu.add_command(label="Salir")



#--------------------------SUBMENUS EDICIÓN-----------------------------
archivoEdicion=Menu(barraMenu)

archivoEdicion.add_command(label="Copiar")

archivoEdicion.add_command(label="Cortar")

archivoEdicion.add_command(label="Pegar")

#--------------------------SUBMENUS HERRAMIENTAS-----------------------------
archivoHerramientas=Menu(barraMenu)


#--------------------------SUBMENUS AYUDA-----------------------------

archivoAyuda=Menu(barraMenu)


archivoAyuda.add_command(label="Licencia")

archivoAyuda.add_command(label="Acerca de")




barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



root.mainloop()

