#Entrada
nombre = input("¿Cuál es tu nombre: ?")
edad = input("¿Cuál es tu edad: ?")

#Salida
print("Me alegro de conocerte {}, Bienvenido... veo que tines {} años".format(nombre,edad))


#escribir un programa que me permita calcular el promedio de tres noras
nota1 = float(input("¿Cuál es tu primer nota?"))
nota2 = float(input("¿Cuál es tu segunda nota?"))
nota3 = float(input("¿Cuál es tu tercer nota?"))

promedio = (nota1+nota2+nota3)/3

print("Tu primer nota es: {}".format(nota1))
print("Tu segunda nota es: {}".format(nota2))
print("Tu tercer nota es: {}".format(nota3))
print("Tu nota promedio es: {}".format(promedio))