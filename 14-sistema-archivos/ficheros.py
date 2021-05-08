from io import open 
import pathlib
import shutil

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

#Escribir dentro de un archivo
archivo.write("****Soy un texto metido en python****\n")

#cerrar archivo
archivo.close()

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

#leer contenido
#contenido = archivo_lectura.read()
# for elemento in contenido:
#     print(elemento)
#print(contenido)

#leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

#print(lista)
for frase in lista:
    #print("- "+frase.upper())
    print("- "+frase.center(100))

#copia archivo
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = "../07-ejercicios/fichero_copiado77.txt"
#shutil.copy(ruta_original, ruta_nueva)
#shutil.copy(ruta_original, ruta_alternativa)

#Mover archivo a otra ruta 
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)
"""

#Eliminar archivos 
import os

ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
os.remove()


