from tkinter import *


root=Tk()

root.title("Ventana para lables")

miFrame=Frame(root,width=500,height=400)

miFrame.pack()


miImagen=PhotoImage(file="paisaje3.gif")

Label(miFrame,image=miImagen)

miLabel.place(x=100,y=200)

root.mainloop()