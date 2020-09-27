from io import *


archivo_texto=open("archivo.txt","r")


archivo_texto.seek(10)

print(archivo_texto.read())





archivo_texto.close()