"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico
nombre.
Paa acceder a esos valores podemos usar un indice numerico
"""

pelicula = "Batman"
#definir lista
peliculas = ["Batman", "Spiderman", "La pasion de Cristo"]
cantantes = list(('Barack', 'Alex Campos', 'Marcos Brunet', 'Miel San Marcos')) #debemos definir con tupla ()
years = list(range(2020, 2050))
variada = ["Julian", 10, 2.5, True, "Texto"]

"""
print(pelicula)
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

#Indices
pelicula = "otra cosa"
peliculas[1] = "Apocalipsis"
print(peliculas)

print(peliculas[1])#salida Spiderman
print(peliculas[-2])#salida Spiderman
print(cantantes[1:3])#sublista de rango de elementos que quiera ver
print(peliculas[1:])#saca todos los elementos de la lista a partir de indice 1

#Añadir elementos a una lista
cantantes.append("Redimido2")
cantantes.append("Julio Melgar")
print(cantantes)

#Recorrer una lista

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("introduce la nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n*****LISTADO DE PELICULAS******")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

