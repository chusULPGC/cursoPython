class Coche():
	def desplazamiento(self):
		print ("Me desplazo usando cuatro ruedas")




class Moto():
	def desplazamiento(self):
		print("Me desplazo usando 2 ruedas")





class Camion():
	def desplazamiento(self):
		print("Me desplazo usando 6 ruedas")






def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()



miVehiculo=Camion()
miVehiculo2=Coche()
miVehiculo3=Moto()

desplazamientoVehiculo(miVehiculo)
desplazamientoVehiculo(miVehiculo2)
desplazamientoVehiculo(miVehiculo3)


