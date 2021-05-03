"""
Ejercicio 1: Hacer un programa que tenga un a lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
-hacer un afuncion que recorra lista de numeros y devuelva un string
- ordenarla y mosrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

# 1er punto---------------------------
#Crear lista
numeros = [15,31,52,49,27,86,77,67]

#Recorrer la lista y mostrarla
print("################### Recorrer y Mostrar ###############")
for numero in numeros:
    print(numero)

#2do punto---------------------------
print("################### recorra lista y devuelva un string ###############")
#Crear funcion que recorra lista y devuelva un string
def mostrarLista(lista):
    resultado = ""
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    return resultado

print(mostrarLista(numeros))

#3ro Ordenar y mostrar
print("############### Ordenar y Mostrar #############")
numeros.sort()
print(mostrarLista(numeros))

#4to mostrar la longitud
print("############## Mostrar Longitud #############")
print(len(numeros))

#4to mostrar la longitud
print("############## Busqueda en la Lista #############")

busqueda = int(input("Introduce el numero: "))

comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el numero: "))
else:
    print(f"Has introducido el {busqueda}")

print(f"#### Buscar en la lista el numero: {busqueda} ####")

search = numeros.index(busqueda)
print(f"El numero buscado existe en la lista, es el indice: {search}")


