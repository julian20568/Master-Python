"""
Ejercicio 9:
    hacer un programa que pida numeros a usuario indefinidamente 
    hasta que introducir el numero 111
"""

contador = 1

#numero = int(input("Ingrese un número: "))

while contador < 100:
    numero = int(input("Ingrese número:"))

    if numero == 111:
        break
    else:
        print("Has introducido el: {}".format(numero))
