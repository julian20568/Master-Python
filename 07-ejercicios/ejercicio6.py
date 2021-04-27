"""
Ejercicio 6. 
    -Mostrar todas las tablas de multiplicar del 1 al 10.
    -Mostrar el titulo de la tabla y luego las multiplicaciones del 1 al 10
"""

for cabecera in range(1, 11):
    print("#######################")
    print("#####Tabla del: {}#####".format(cabecera))
    print("#######################")

    for numero in range(1, 11):
        print("{} X {} = {} ".format(numero, cabecera, numero * cabecera))



