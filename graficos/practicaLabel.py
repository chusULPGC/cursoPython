from tkinter import *


root=Tk()

root.title("Ventana para lables")

miFrame=Frame(root,width=500,height=400)

miFrame.pack()


miLabel=Label(miFrame,text="Hola alumnos de python", fg="red", font=("Comic Sans MS",18))

miLabel.place(x=100,y=200)

root.mainloop()