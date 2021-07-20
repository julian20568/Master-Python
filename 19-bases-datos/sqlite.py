#importar el modulo
import sqlite3

#conexion 
conexion = sqlite3.connect('pruebas.db')

#crear cursor
cursor = conexion.cursor()

#crear una tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
    "id integer PRIMARY KEY AUTOINCREMENT,
    "titulo varchar(255),
    "descripcion text, 
    "precio int(255)
);
""")

#Guardar cambios
conexion.commit()

#Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Primer Producto', 'Descripcion de mi producto', 550)")
conexion.commit()
"""

#Borrar registros
#cursor.execute("DELETE FROM productos;")
#conexion.commit()

#Insertar muchos registros de golpe
productos = [
    ("Ordenador Portatil", "Buen PC", 700),
    ("Telefono movil", "Buen Telefono", 140),
    ("Placa base", "Buena placa", 80),
    ("Tablet 15", "Buena tablet", 300)
]

cursor.executemany("INSERT INTO productos VALUES (null, ?,?,?)", productos)
conexion.commit()

#Actualizar registros
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")

#Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 100;")
#print(cursor)
productos = cursor.fetchall()

#print(productos)
for producto in productos:
    #print(producto)
    print("ID: ", producto[0])
    print("Titulo:", producto[1])
    print("Descripcion:", producto[2])
    print("Precio:", producto[3])
    print("\n")

#sacar el primer registro de la tabla
cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)

#cerrar la conexion
conexion.close()