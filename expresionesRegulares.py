import re


print("\n-----------------Empezamos con el metodo search()-------------------\n")
cadena="Vamos a aprender expresiones regulare en Python. Python es un lenguaje de sintaxis sencilla. Python es cojonudo"

print(re.search("aprender",cadena))


textoBuscar="Python"

if re.search(textoBuscar,cadena) is not None:
	print("He encontrado el texto")
else:
	print("No he encontrado el texto")



print("\n-----------------Vamos a probar el metodo start()-------------------\n")
textoEncontrado=re.search(textoBuscar,cadena)

print(textoEncontrado.start())


print("\n-----------------Vamos a probar el metodo end()-------------------\n")
textoEncontrado=re.search(textoBuscar,cadena)

print(textoEncontrado.end())


print("\n-----------------Vamos a probar el metodo span()-------------------\n")
textoEncontrado=re.search(textoBuscar,cadena)

print(textoEncontrado.span())

print("\n-----------------Vamos a probar el metodo findall()-------------------\n")

print(re.findall(textoBuscar,cadena))