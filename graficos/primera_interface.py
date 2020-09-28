from tkinter import *


raiz=Tk()

raiz.title("Ventana de pruebas")



raiz.config(bg="blue")

miFrame=Frame()

miFrame.pack(fill="both", expand=True)

miFrame.config(bg="red")


miFrame.config(width="650", height="350")


miFrame.config(bd=35)

miFrame.config(relief="groove")

miFrame.config(cursor="pirate")

raiz.mainloop()

