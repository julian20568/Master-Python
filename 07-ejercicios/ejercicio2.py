"""
Ejercicio 2:
    Escribir un escript que nos muestre por pantalla
    todos los numeros pares del 1 al 120
"""

contador = 1

for contador in range(1, 120):
    if contador%2 == 0:
        print("{} Es Número par".format(contador))
    # else:
    #     print("{} Es Número impar".format(contador))
