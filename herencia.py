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



class Furgoneta(Vehiculos):
	def carga(self,cargar):
		self.cargado=cargar
		if(self.cargado==True):
			return "La Furgoneta está cargada"
		else:
			return "La Furgoneta no está cargada"




class Moto(Vehiculos):
	hcaballito=""

	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"


	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelarando: ",self.acelera, "\nFrenando: ",self.frena,"\n", self.hcaballito)



class VElectricos(Vehiculos):
	def __init__(self,marca,modelo):

		super().__init__(marca,modelo)
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True



print ("--------------------------------------------Creamos objeto Moto--------------------------------------------")

miMoto=Moto("Honda","CBR")


miMoto.caballito()


miMoto.estado()

print ("--------------------------------------------Creamos objeto Furgoneta--------------------------------------------")

miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print ("\n",miFurgoneta.carga(True))



class BicicletaElectrica(VElectricos,Vehiculos):
	pass


miBici=BicicletaElectrica("BH","Top Line")























