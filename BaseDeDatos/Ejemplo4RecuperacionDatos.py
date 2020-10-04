import sqlite3


#los pasos son los siguientes:
# 1) abrir-crear conexion
# 2) Crear puntero,cursor
# 3) Ejecutar query(consulta) SQL
# 4) Manejar los resultados de la query(consulta) -->insertar,leer,actualizar,borrar(CRUD)
# 5) Cerrar el puntero,cursor
# 6) Cerrar conexion
 


miConexion=sqlite3.connect("PrimeraBase")#en el mismo comando creamos y abrimos la BBDD

miCursor=miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS")

#creamos una lista para almacenar los datos del select

variosProductos=miCursor.fetchall()


for producto in variosProductos:
	print(producto)

print("\n-------------------OTRA FORMA DE MOSTRAR------------------------------------\n")
for producto in variosProductos:
	print("NOMBRE ARTICULO: "+producto[0], ",PRECIO: "+str(producto[1]), ",SECCIÓN: "+producto[2])


miConexion.commit()

miConexion.close()