"""
Modulos: son funcionalidaes ya hechas para realizar
En python hay muchos modulos, que los puedes consultar aqui:
https://docs.python.org/3/library/math.html#module-math

podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internte, tambien podemos crear nuestros modulos
"""

#importar modulo propio
import mimodulo

#como utilizo mis finciones
print(mimodulo.holaMundo("Julian Obando"))
print(mimodulo.calculadora(3, 5, True))

#importar una sola funcion
from mimodulo import holaMundo

print(holaMundo("Julian Obando"))

#importar todos lo que hay en mi modulo prop
from mimodulo import *
print(calculadora(3, 5, True))

#Modulo de fechas
import datetime
print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%Y-%m-%d, %H:%M:%S")
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp())

#modulo matematicas

import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Numero pi: ", float(math.pi))
print("Redondear Arriba: ", math.ceil(6.56798))#arriba
print("Redondear Abajo: ", math.floor(6.56798))#abajo

#modulo randon
import random
print("Numero aleatorio entre 15 y 67: ", random.randint(15, 67))