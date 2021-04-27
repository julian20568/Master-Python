"""
Ejercicio8:
    Cuanto es el X por ciento de X numero
                 20%   de       150
"""

numero = int(input("Ingrese un número: "))
porcentaje = int(input("Que porcentaje quieres sacar de {}: ".format(numero)))

operacion = (numero * (porcentaje /100))

print("El {}%, de {} es: {}".format(porcentaje, numero, operacion))

