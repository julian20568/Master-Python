"""
Ejercicio5:
    Hacer un programa que muestre todos los numeros entre 
    dos numeros que ingrese el  usuario
"""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 < num2:

    for contador in range(num1, (num2 + 1)):
        print(contador)
else:
    print("El numero 1 debe ser menor al numero 2")