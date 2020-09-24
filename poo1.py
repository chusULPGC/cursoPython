
class Coche():

	def __init__(self):
		self.__largoChasis=250
		self.__ancho=120
		self.__ruedas=4 
		self.__enMarcha=False



	def arrancar(self,arrancamos):
		self.enMarcha=arrancamos
		if (self.enMarcha==True):
			return "Arrancado"
		else:
			return "Apagado"



	def estado(self):
		print "El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__ancho, " y un largo de ", self.__largoChasis


miCoche=Coche()

print (miCoche.arrancar(True))
miCoche.estado()

print (".........................................A continuación creamos el segundo objeto.........................................")

miCoche2=Coche()

print (miCoche2.arrancar(False))
miCoche2.estado()

