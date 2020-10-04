import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()


miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'")


productos=miCursor.fetchall()

print(productos)


miCursor.execute("UPDATE PRODUCTOS SET precio=35 WHERE NOMBRE_ARTICULO='pelota'")

miCursor.execute("SELECT * FROM PRODUCTOS WHERE NOMBRE_ARTICULO='pelota'")

productos=miCursor.fetchall()

print(productos)

miCursor.execute("DELETE FROM PRODUCTOS WHERE id=5")
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'")

productos=miCursor.fetchall()

print(productos)




miConexion.commit()


miConexion.close()