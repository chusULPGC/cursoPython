from tkinter import *
import math  



raiz=Tk()

raiz.config(bg="#F5F3F3")

raiz.title("Calculadora")


miFrame=Frame(raiz)

miFrame.config(bg="#F5F3F3")
miFrame.pack()

operacion=""

reset_pantalla=False

resultado=0

#..................................PANTALLA FILA 1.........................................

numeroPantalla=StringVar()


pantalla=Entry(miFrame, textvariable=numeroPantalla)

pantalla.grid(row=1, column=1,padx=10, pady=10, columnspan=4)

pantalla.config(background="white", fg="black", justify="left")


#..................................PULSACIONES TECLADO.................................


def limpiarPantalla():
	numeroPantalla.set("")

def raizCuadrada():
	global resultado
	numeroPantalla.set(math.sqrt(float(numeroPantalla.get())))

def factorial():
	numeroPantalla.set(math.factorial(float(numeroPantalla.get())))


def cuadrado():
	numeroPantalla.set(pow((float(numeroPantalla.get())),2))


def numeroPulsado(num):
	global operacion
	global reset_pantalla
	if reset_pantalla!=False:
		numeroPantalla.set(num)
		reset_pantalla=False
	else:
		numeroPantalla.set(numeroPantalla.get()+num)#get dentro de set es para que primero pille lo que hay en pantalla y concatene
												#con lo que pulsamosç


#------------------------------ SUMA -----------------------------------

def suma(num):
	global operacion
	global resultado
	global reset_pantalla
	resultado+=float(num)
	operacion="suma"
	reset_pantalla=True
	numeroPantalla.set(resultado)



#------------------------------ RESTA -----------------------------------

num1=0
contador_resta=0
def resta(num):
	global resultado
	global operacion
	global num1
	global contador_resta
	global reset_pantalla

	if contador_resta==0:
		num1=float(num)
		resultado=num1
	else:
		if contador_resta==1:
			resultado=num1-float(num)
		else:
			resultado=float(resultado)-float(num)
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	contador_resta=contador_resta+1
	operacion="resta"
	reset_pantalla=True


#------------------------------ MULTIPLICACIÓN -----------------------------------

contador_multi=0

def multiplica(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla
	
	if contador_multi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*float(num)

		else:

			resultado=float(resultado)*float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_multi=contador_multi+1

	operacion="multiplicacion"

	reset_pantalla=True

#-----------------funcion division---------------------

contador_divi=0

def divide(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_divi=contador_divi+1

	operacion="division"

	reset_pantalla=True



#--------------------funcion el_resultado---------------------------------------------

def el_resultado():

	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi
	

	if operacion=="suma":

		numeroPantalla.set(resultado+float(numeroPantalla.get()))

		resultado=0

	elif operacion=="resta":

		numeroPantalla.set(float(resultado)-float(numeroPantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicacion":

		numeroPantalla.set(float(resultado)*float(numeroPantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="division":

		numeroPantalla.set(float(resultado)/float(numeroPantalla.get()))

		resultado=0

		contador_divi=0











#..................................FILA 2.........................................

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)

boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)

boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)

botonDividir=Button(miFrame, text="/", width=3, command=lambda:divide(numeroPantalla.get()))
botonDividir.grid(row=2,column=4)

#..................................FILA 3.........................................

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)

boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)

boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)

botonMultiplicar=Button(miFrame, text="X", width=3,command=lambda:multiplica(numeroPantalla.get()))
botonMultiplicar.grid(row=3,column=4)


#..................................FILA 4.........................................

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)

boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)

boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)

botonRestar=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRestar.grid(row=4,column=4)

#..................................FILA 5.........................................

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)

botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado("."))
botonComa.grid(row=5,column=2)

botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5,column=3)

botonSumar=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
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

















