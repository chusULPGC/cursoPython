
print "Programa para comprobar nota"

nota_alumno=input()

def evaluacion(nota):
	if nota>10 or nota < 0: 
		return "imposible"
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion

print evaluacion(nota_alumno)


