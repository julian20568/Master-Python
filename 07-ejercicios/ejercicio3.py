"""
Ejercicio 3:
    Escribir un programa que muestre los cuadrados
    (un número multiplicado por si mismo) de los 60 primeros números
    naturales. Resolver con for y con while.
"""

#WHILE

# contador = 0
# while contador <= 60:
#     cuadrado = contador * contador
#     print("El cuadrado de: {} es {}".format(contador, cuadrado))

#     contador += 1

for numero in range(61):
    cuadrado = numero * numero
    print("El cuadrado de: {} es {}".format(numero, cuadrado))
