"""
# FOR

for variable in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES
"""

contador = 0
resultado = 0

for contador in range(0, 5):
    print("Voy por el: {}".format(contador))

    #resultado = resultado + contador
    resultado += contador

print('El resultado es: {}'.format(resultado))

#Ejemplo de tablas de multiplicar
print("\n#######################EJEMPLO#######################")

numero_usuario = int(input("¿De que número quieres la tabla?"))

if numero_usuario < 1:
    numero_usuario = 1

print("## Tabla de multiplicar del numero: {}".format(numero_usuario))

for numero_tabla in range(1, 11):

    if numero_usuario == 45:
        print("No se pueden mostrar números prohibidos !! ")
        break #corta el cico
    print("{} X {} = {}".format(numero_usuario, numero_tabla, numero_usuario * numero_tabla))
else:
    print("Tabla finalizada")