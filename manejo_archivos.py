from io import *

archivo_texto=open("archivo.txt","w")

frase="Estupendo día para estudiar python \n el domingo"

archivo_texto.write(frase)

archivo_texto.close()