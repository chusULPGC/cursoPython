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







