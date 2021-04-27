"""
Ejercicio10:
    El programa tiene que pedir la nota d 15 alumnos
    y sacar por pantalla cuantos han aprobado y cuantos han suspendido
"""

contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuantos alumnos tienes: ?"))

while contador <= numero_alumnos:
    nota = int(input("¿Que nota quieres ponerle al \"alumno{}\" ?".format(contador)))

    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1

    contador += 1

print("Alumnos aprobados {}: ".format(aprobados))
print("Alumnos suspendidos {}: ".format(suspendidos))