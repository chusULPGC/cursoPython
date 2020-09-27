from io import *

archivo_texto=open("archivo.txt","r")

texto=archivo_texto.readlines()

archivo_texto.close()

print(texto)
