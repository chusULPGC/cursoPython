import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()


#añadiendo unique al campo nombre_articulo evitamos que se repitan articulos con el mismo nombre
miCursor.execute('''
CREATE TABLE PRODUCTOS (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NOMBRE_ARTICULO VARCHAR(50) UNIQUE, 	
PRECIO INTEGER,
SECCION VARCHAR(20))
''')


productos=[
	("pelota",20,"juguetería"),
	("pantalón",15,"confección"),
	("destornillador",25,"ferretería"),
	("jarrón",45,"cerámica"),
	("pantalones",30,"confección")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)




miConexion.commit()


miConexion.close()