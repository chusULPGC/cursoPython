import re

lista_nombres=['Ana',
				'Pedro',
				'María',
				'Rosa',
				'Sandra',
				'Celia',
				'ana',
				'pedro',
				'maría',
				'rosa',
				'sandra',
				'celia',
				]


print("--------todos los elementos de la lista que contienen letras entre la o y la t\n")
for elemento in lista_nombres:
	if re.findall('[o-t]',elemento): #rango entre la o y la t (o,p,q,r,s,t)
		print(elemento)


print("\n--------todos los elementos de la lista empiezan con letras comprendidas entre la o y la t\n")

for elemento in lista_nombres:
	if re.findall('^[O-T]',elemento): #rango entre la o y la t (o,p,q,r,s,t)
		print(elemento)


print("\n--------todos los elementos de la lista que NO tienen letras comprendidas entre la o y la t\n")

for elemento in lista_nombres:
	if re.findall('^[^O-T]',elemento): #rango entre la o y la t (o,p,q,r,s,t)
		print(elemento)


print("\n--------todos los elementos de la lista empiezan con letras comprendidas entre la o y la t mayusculas y minusculas\n")


for elemento in lista_nombres:
	if re.findall('^[O-To-t]',elemento): #rango entre la o y la t (o,p,q,r,s,t)
		print(elemento)







