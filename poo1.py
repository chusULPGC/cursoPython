
class Coche():

	def __init__(self):
		self.__largoChasis=250
		self.__ancho=120
		self.__ruedas=4 
		self.__enMarcha=False



	def arrancar(self,arrancamos):
		self.__enMarcha=arrancamos

		if (self.__enMarcha==True):
			chequeo=self.chequeo_interno() #chequeo almacena true o false dependiendo de chequeo_interno()

		if (self.__enMarcha==True and chequeo==True):
			return "Arrancado"
		elif(self.__enMarcha==True and chequeo==False):
			return "Algo ha ido mal en el chequeo. No se puede arrancar"
		else:
			return "Apagado"



	def estado(self):
		print "El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__ancho, " y un largo de ", self.__largoChasis



	def chequeo_interno(self):
		print "Realizando chequeo interno"
		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False



miCoche=Coche()

print (miCoche.arrancar(True))
miCoche.estado()

print (".........................................A continuación creamos el segundo objeto.........................................")

miCoche2=Coche()

print (miCoche2.arrancar(False))
miCoche2.estado()

