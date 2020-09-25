

def suma():
	print "primer numero"
	a=int(input())
	print "segundo numero"
	b=int(input())
	print "La suma es",a+b


def resta():
	print "primer numero"
	a=int(input())
	print "segundo numero"
	b=int(input())
	print "La resta es",a-b



def multiplicacion():
	print "primer numero"
	a=int(input())
	print "segundo numero"
	b=int(input())
	print "La multiplicacion es",a*b



def division():
	print "primer numero"
	a=int(input())
	print "segundo numero"
	b=int(input())
	print "La divison es",a/b



def eleccion():
	operacion=input("Que desea hacer, suma,resta,multiplicacion,division")
	
	if (operacion==suma):
		suma()
	if (operacion==resta):
		resta()
	if (operacion==multiplicacion):
		multiplicacion()
	if (operacion==division):
		division()
    
eleccion()

