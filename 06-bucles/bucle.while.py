"""
#BUCLE WHILE
Estructura de control que itera o repite la ejecución de una
serie de instrucciones tantas veces coo sea necesario,
hasta que deje de cumplirse la condición

while condicion:
    bloque de instrcciones
    actualizacion de contador
"""

contador = 1

while contador <= 100:
    print("Estoy en el número: {}".format(contador))
    contador = contador + 1

print("\n------------------------------------------")

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador = contador + 1

print(muestrame)

print("\n------------------------------------------")

numero_usuario = int(input("¿De que número quieres la tabla: ?"))

if numero_usuario < 1:
    numero_usuario = 1

print("### Tabla del: {} ###".format(numero_usuario))

contador = 1
while contador <= 10:
    print("{} X {} = {} ".format(numero_usuario, contador, numero_usuario * contador))
    contador += 1
else:
    print("Tabla finalizada")