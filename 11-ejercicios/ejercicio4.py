"""
Ejercicio 4: Crear un script que tenga cuatro variables,
una lista, un string,
un entero y un booleano y que imprima
un mensaje segun el tipo de dato de cada variable. Usar funciones
"""

def comprobarTipado(dato, tipo):
    test = isinstance(dato,tipo)
    result = ""

    if result:
        result = f"Este dato es de tipo {type(dato)}"
    else:
        result = None
    return result

lista = ["Real Madrid", "Barcelona", "Atletico de Madrid", "Betis", "Chelse"]
string = "Julian Obando"
entero = int(20)
booleano = True

print(comprobarTipado(lista, list))

#Funcion para mostrar lista
def getLista(lista):
    texto = (f"La lista de equipos es: {lista}")
    return texto

#Funcion para mostrar string
def getString(string):
    texto = (f"El String es: {string}")
    return texto

#Funcion para mostrar un entero
def getEntero(entero):
    texto = (f"El enetro es: {entero}")
    return texto

#Funcion para mostrar un booleano
def getBool(booleano):
    texto = (f"El Booleano es: {booleano}")
    return texto

def mostrarTodo(lista, string, entero, booleano):
    texto = getLista(type(lista)) + "\n" + getString(type(string)) + "\n" + getEntero(type(entero)) + "\n" +getBool(type(booleano))
    #texto = "Listas: " + str(lista) + "\n" + "String: " + str(string) + "\n" + "Entero: " + int(entero) + "\n" + bool(booleano)
    return texto

print(getLista(lista))
print(getString(string))
print(getEntero(entero))
print(getBool(booleano))
print(mostrarTodo(lista, string, entero, booleano))
