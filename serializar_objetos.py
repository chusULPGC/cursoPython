import pickle




class Vehiculos():
	def __init__(self,marca,modelo):
		self.marca=marca
		self.modelo=modelo
		self.enMarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enMarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelarando: ",self.acelera, "\nFrenando: ",self.frena,) 


coche1=Vehiculos("Renault","Megane")

coche2=Vehiculos("Seat","Leon")

coche3=Vehiculos("Tesla","Model S")


coches=[coche1,coche2,coche3]


fichero=open("LosCoches","wb")

pickle.dump(coches,fichero)




fichero.close()

del(fichero)

ficheroApertura=open("LosCoches","rb")

misCoches=pickle.load(ficheroApertura)


for i in misCoches:
	print(i.estado())


ficheroApertura.close()















