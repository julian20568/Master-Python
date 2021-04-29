"""
FUNCIONES:
Una funcion es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden utilizarse invocando a la función
tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
    #BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)

"""

#Ejemplo 1

#definir función
print("#########EJEMPLO1##########")

def muestraNombre():
    print("Julián")
    print("Carlos")
    print("Juan")
    print("Hector")
    print("Martin") 
    print("\n")

#invocar la función
muestraNombre()

#Ejemplo 2

print("#########EJEMPLO2##########")

def mostrarTuNombre(nombre, edad):
    print("tu nombre es: {}".format(nombre))

    if edad >= 18:
        print("y eres mayor de edad")
    else:
        print("Y eres menor de edad")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))      
mostrarTuNombre(nombre, edad)

#Ejemplo 3

print("#########EJEMPLO3##########")

def tabla(numero):
    print("Tabla de multiplicar del número {}: ".format(numero))

    for contador in range(11):
        #operacion = numero * contador
        print("{} X {} = {} ".format(numero, contador, numero * contador))
    
    print("\n")

tabla(5)
tabla(7)
tabla(12)

#Ejemplo 3.1
print("---------------------------------------")
for numero_tabla in range(1, 11):
    tabla(numero_tabla)

#Ejemplo 4

print("#########EJEMPLO4##########")

#parametros opcionales

def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print("{}".format(nombre))

    if dni != None:
        print("{}".format(dni))

getEmpleado("Julian")

#Ejemplo 5: return o devolver datos

print("#########EJEMPLO5##########")
def saludame(nombre):
    saludo = "Hola, saludos {} ".format(nombre)

    return saludo

print(saludame("Julian Obando"))

#Ejemplo 6: 

print("#########EJEMPLO6##########")

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta:" + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena

print(calculadora(5, 10, True)) # saca las operaciones basicas
#print(calculadora(5, 10, False)) # saca multiplicacion y division

#Ejemplo 7: funciones dentro de otras

print("#########EJEMPLO7##########")

def getNombre(nombre):
    texto = "El nombre es {}: ".format(nombre)
    return texto

def getApellidos(apellidos):
    texto = "Los apellidos son {}: ".format(apellidos)
    return texto

def devulveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

#print(getNombre("Julian Andres"), getApellidos("Obando Palechor"))
print(devulveTodo("Julian", "Obando"))

#Ejemplo 8: funciones lambda

print("#########EJEMPLO8##########")

dime_el_year = lambda year: "El años es {}: ".format(year) #dentro del parametro puedo hacer operaciones

print(dime_el_year(2034))