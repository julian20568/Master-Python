"""
Diccionario:
Es un tipo de datos que almacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json
"""

persona = {
    "nombre": "Julian",
    "apellidos":"Obando",
    "web":"julianobandoweb.es"
}

print(persona)
print(persona["apellidos"])#acceder a un indice especifico

#Lista con diccionarios

contactos = [
    {
        'nombre':'Julian',
        'email':'jaop17@hotmail.com'
    },
    {
        'nombre':'Andres',
        'email':'andres@andres.com'
    },
    {
        'nombre':'Salvador',
        'email':'salvador@salvador.com'
    }
]

print(contactos)
contactos[0]['nombre'] = "Juliano"#cambiar nombre
print(contactos[0]['nombre'])

print("\nListado de contactos")
print("----------------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("----------------------------------------")