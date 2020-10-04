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

variosProductos=[
	("Camiseta",10,"Deportes"),
	("Jarrón",90,"Cerámica"),
	("Camión",10,"Juguetería")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)


miConexion.commit()

miConexion.close()