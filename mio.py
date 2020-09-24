
correo=input("Que quiere contar: ")
correo=correo.lower()

def bucle(mail):
	lista=""
	abc="abcdefghijklmnopqrstuvwxyz123456789,.-() "
	for i in abc:
		suma=0
		for x in mail:
			if i==x:
				suma=suma+1
		print str(i)+"="+str(suma)
		lista=lista+str(i)+"="+str(suma)
	return lista
		
		

bucle(correo)