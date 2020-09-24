#encoding: utf-8

print "Introduzca un correo electrónico"
correo=input()

def login(mail):
	ristra=""
	for i in mail:
		if(i!="@"):
			ristra=ristra+i
		else:
			break
	return ristra




def dominio(mail):
	dom=""
	for i in reversed(mail):
		if(i!="@"):
			dom=i+dom
		else:
			break
	return dom 



print login(correo)
print dominio(correo)
