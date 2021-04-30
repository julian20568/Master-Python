cantantes = ['Rober Green', 'Alex Campos', 'Luis Campos', 'Marcos Brunet']
numeros = [1, 2, 5, 8, 3, 4, 7, 6]
#print(numeros)
#numeros.sort()
#print(numeros)

#Añadir elementos
cantantes.append("Miel San Marcos y Marcos barrientos")
cantantes.insert(1, "Julio Melgar")
#print(cantantes)

#Eliminar elementos de una lista
cantantes.pop(1)
cantantes.remove("Luis Campos")
#print(cantantes)

#dar la vuelta
#print(numeros)
numeros.reverse()
#print(numeros)

#Buscar dentro de una lista
print('Alex Campos' in cantantes)

#contar elementos
print(len(cantantes))

#cuantas veces un elemento en la lista
print(numeros.count(8))

#conseguir indice
print(cantantes.index("Marcos Brunet"))

#unir listas
cantantes.extend(numeros)
print(cantantes)
