
class Empleado:
	def __init__(self,nombre,cargo,salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario


	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {}€".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[

Empleado("Juan","Director",5000),


Empleado("Duna","Presidenta 1",8000),


Empleado("Rut","Presidenta 2",8000),


Empleado("Chus","Mozo de cuadra",900)

]


def calculo_comision(empleado):
	if(empleado.salario<=3000):
		empleado.salario=empleado.salario*1.03 #la comision de los empleados que cobran menos de 3000 va a tener una comision de un 3%
	return empleado

listaComision=map(calculo_comision,listaEmpleados)


for empleado in listaComision:
	print(empleado)

