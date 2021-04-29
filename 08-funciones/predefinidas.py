nombre = "Julian Obando"

#funciones generales
print(type(nombre))

#detectar el tipado

comprobar =isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

#Limpiar espacios
frase = "    mi contenido    "
print(frase)
print(frase.strip())#limpia todos los espacios

#Eliminar variables
year = 2022
print(year)
del year #elimina la variable
#print(year)

#comprobar variable vacia

texto = "   fff   "
if len(texto) <= 0:
    print("la variable esta vacia")
else:
    print("la variable tiene contenido: ", len(texto))

#encontrar caracteres dentro de un String

frase = "La vida es bella"
print(frase.find("vida"))

#Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

#Mayusculas y Minusculas
print(nombre)
print(nombre.lower())#convierte a minusculas
print(nombre.upper())#convierte a mayusculas
