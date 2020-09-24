
tupla=("Chus","Izquierdo",14,5,1987)
lista=list(tupla)

print lista

tupla=tuple(lista)

print tupla

print ("Chus" in tupla)

print tupla.count("Chus")

print len(tupla)

for x in range(len(tupla)):
	print tupla[x]

nombre, apellido, day, month, year=tupla #desenpaquetado de tuplas


print nombre
print apellido
print day
print month
print year



