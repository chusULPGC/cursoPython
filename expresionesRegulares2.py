import re

lista_nombres=['Ana Gómez',
				'María Martín',
				'Sandra López',
				'Santiago Martín',
				'http://pildorasinformaticas.es',
				'ftp://pildorasinformaticas.es',
				'http://pildorasinformaticas.com',
				'http://google.es',
				'http://informaticaenespaña.com',
				'niños',
				'niñas'
				]

print("--------todos los que empiezan por S-------------\n")
for elemento in lista_nombres:
	if re.findall('^S',elemento):
		print(elemento)



print("--------todos los que terminan por n-------------\n")
for elemento in lista_nombres:
	if re.findall('n$',elemento):
		print(elemento)


print("--------todos los dominios que terminan en .es-------------\n")
for elemento in lista_nombres:
	if re.findall('es$',elemento):
		print(elemento)		



print("--------todos los dominios que son ftp-------------\n")
for elemento in lista_nombres:
	if re.findall('^ftp',elemento):
		print(elemento)		


print("--------todas lo que contengan una ñ-------------\n")
for elemento in lista_nombres:
	if re.findall('[ñ]',elemento):
		print(elemento)



print("--------todas lo que contengan una ño ña-------------\n")
for elemento in lista_nombres:
	if re.findall('niñ[oa]s',elemento):
		print(elemento)