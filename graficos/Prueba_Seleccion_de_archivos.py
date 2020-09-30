from tkinter import *
from tkinter import filedialog


root=Tk()

def abreFichero():
	fichero=filedialog.askopenfilename(title="Abrir")#este metodo devuelve la ruta del fichero que abres
	print(fichero)



Button(root,text="Abrir fichero", command=abreFichero).pack()






root.mainloop()