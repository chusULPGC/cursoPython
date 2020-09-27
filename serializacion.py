import pickle 

lista_nombres=["Chus","Rut","Duna"]

fichero_binario=open("lista_nombres","wb")


pickle.dump(lista_nombres,fichero_binario)


fichero_binario.close()