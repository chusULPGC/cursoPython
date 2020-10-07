

class Empleado:
	def __init__(self,nombre,cargo,salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario


	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {}€".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[

Empleado("Juan","Director",75000),


Empleado("Duna","Presidenta 1",85000),


Empleado("Rut","Presidenta 2",85000),


Empleado("Chus","Mozo de cuadra",15000)
]



print("---------------Empleados con salarios altos---------------------------")
salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleado_salario in salarios_altos:
	print(empleado_salario)




print("\n---------------Empleados pobres---------------------------")

salarios_bajos=filter(lambda empleado:empleado.salario<50000, listaEmpleados)

for empleado_salario in salarios_bajos:
	print(empleado_salario)
