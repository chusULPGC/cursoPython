class Persona():
	
	def __init__(self,nombre,edad,residencia):
		self.nombre=nombre
		self.edad=edad
		self.residencia=residencia



	def descripcion(self):
		print ("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.residencia)



class Empleado(Persona):

	def __init__(self,salario,antigüedad,nombre_empleado,edad_empleado,residencia_empleado):

		super().__init__(nombre_empleado,edad_empleado,residencia_empleado)

		self.salario=salario
		self.antigüedad=antigüedad


	def descripcion(self):
		super().descripcion()
		print("Salario: ",self.salario,"\nAntigüedad: ",self.antigüedad)




Antonio=Persona("Antonio",35,"España")
Jesus=Empleado(2000,10,"Jesus",33,"Españita")

Antonio.descripcion()

print (isinstance(Antonio,Empleado))

