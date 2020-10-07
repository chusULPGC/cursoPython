def numero_par(num):
	if num % 2==0:
		return True

numeros=[17,24,39,8,51,92]

print(list(filter(numero_par,numeros)))

def numero_impar(num):
	if num % 2!=0:
		return True


print(list(filter(numero_impar,numeros)))


# LO MISMO CON FUNCIONES LAMBDA


print(list(filter(lambda par: par%2==0,numeros)))


print(list(filter(lambda impar: impar%2!=0,numeros)))



print("---------------ahora vamos a filtrar objetos---------------------------")

class Empleado:
	def __init__(Self,nombre,cargo,salario):
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




salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleado_salario in salarios_altos:
	print(empleado_salario)




