from tkinter import *
import math  



raiz=Tk()

raiz.config(bg="#F5F3F3")

raiz.title("Calculadora")


miFrame=Frame(raiz)

miFrame.config(bg="#F5F3F3")
miFrame.pack()


#..................................PANTALLA FILA 1.........................................

numeroPantalla=StringVar()


pantalla=Entry(miFrame, textvariable=numeroPantalla)

pantalla.grid(row=1, column=1,padx=10, pady=10, columnspan=4)

pantalla.config(background="white", fg="black", justify="left")


#..................................PULSACIONES TECLADO.................................
def limpiarPantalla():
	numeroPantalla.set("")

def raizCuadrada():
	numeroPantalla.set(math.sqrt(int(numeroPantalla.get())))

def factorial():
	numeroPantalla.set(math.factorial(int(numeroPantalla.get())))


def cuadrado():
	numeroPantalla.set(pow((int(numeroPantalla.get())),2))




def numeroPulsado(num):
	numeroPantalla.set(numeroPantalla.get()+num)#get dentro de set es para que primero pille lo que hay en pantalla y concatene
												#con lo que pulsamos



#..................................FILA 2.........................................

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)

boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)

boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)

botonDividir=Button(miFrame, text="/", width=3)
botonDividir.grid(row=2,column=4)

#..................................FILA 3.........................................

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)

boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)

boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)

botonMultiplicar=Button(miFrame, text="X", width=3)
botonMultiplicar.grid(row=3,column=4)


#..................................FILA 4.........................................

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)

boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)

boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)

botonRestar=Button(miFrame, text="-", width=3)
botonRestar.grid(row=4,column=4)

#..................................FILA 5.........................................

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)

botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado("."))
botonComa.grid(row=5,column=2)

botonIgual=Button(miFrame, text="=", width=3)
botonIgual.grid(row=5,column=3)

botonSumar=Button(miFrame, text="+", width=3)
botonSumar.grid(row=5,column=4)

#..................................FILA 6.........................................


botonLimpiar=Button(miFrame, text="AC",width=3, command=lambda:limpiarPantalla())
botonLimpiar.grid(row=6, column=1)

botonRaiz=Button(miFrame, text="√",width=3, command=lambda:raizCuadrada())
botonRaiz.grid(row=6, column=2)


botonCuadrado=Button(miFrame, text="x^2",width=3, command=lambda:cuadrado())
botonCuadrado.grid(row=6, column=3)

botonFactorial=Button(miFrame, text="X!",width=3, command=lambda:factorial())
botonFactorial.grid(row=6, column=4)


raiz.mainloop()

















