import mysql.connector

#Conexion
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="master_python"
)

#¿La conexión ha sido correcta?
#print(database)

#crear la base de datos
cursor = database.cursor(buffered=True)

"""
#Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""

#Crear tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10, 2) not null,
    CONSTRAINT pk_vehiculos PRIMARY KEY (id)
)
""")

"""
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

"""

#Insertar datos en la tabla
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")

#Insertar datos de manera masiva
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
database.commit()

#Listar Registros
#cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat' ")
cursor.execute("SELECT * FROM vehiculos")

result = cursor.fetchall()

print("----- TODOS MIS COCHES -----")
for coche in result:
    print(coche[1], coche[2], coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)

#Borrar registros
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes' ")
database.commit()

print(cursor.rowcount, "borrados!!")

#Actualizar registros
cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE marca='Seat'")
database.commit()

print(cursor.rowcount, "actualizados!!")