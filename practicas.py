# Crear un programa que le permita al usuario imprimir
# n tablas de multiplicar segun la cantidad que desee
from builtins import print

n = int(input("numero de tablas que desea imprimir? "))

for cantidad in range(n, 1):
    numero = int(input("Ingrese la tabla {}: ".format(cantidad)))

    for tabla in range(1, 11):
        print("{} X {} = {}".format(numero, tabla, numero * tabla))

"""

"""

print("Pruebas commit")
