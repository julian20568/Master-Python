"""
# CONDICIONAL IF

SI se_cumple_esta_condición:
    ejecuta grupo de instrucciones
SI NO:
    se ejecuta otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones
"""

#ejemplo 1

print("#######################EJEMPLO 1#######################")

#color = "rojo" #entra al if
#color = "verde" #entra al else

#EJEMPLO 1
# color = input("Adivina cuál es mi color favorito")

# if color == "rojo":
#     print("En hora buena!!")
#     print("El color es ROJO")
# else:
#     print("El color es incorrecto")

#EJEMPLO 2
#validar si una persona es mayor de edad

# edad = int(input("Ingresa tu edad: "))

# if edad >= 18:
#     print("Eres mayor de edad, Puedes continuar")
# else:
#     print("Lo siento!!! Eres menor de edad por lo tanto no puedes seguir.")

#EJEMPLO 3
#Calcular la edad de una persona y decir a que categoria pertenece segun su edad

nombre = input("Ingresa tu nombre:")
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
año_actual = int(input("ingrese el año actual: "))

edad = año_actual - año_nacimiento
if edad >= 1 and edad < 7:
    print("{}: Su edad es: {} años, Usted pertenece a la categorias de niños".format(nombre,edad))
elif edad >= 7 and edad < 12:
    print("{}: Su edad es: {} años, Usted pertenece a la categoria de pre-adolesecentes".format(nombre,edad))
elif edad >= 12 and edad < 18:
    print("{}: Su edad es: {} años, Usted pertenece a la categoria de adolescentes".format(nombre,edad)) 
elif edad >= 18 and edad < 30:
    print("{}: Su edad es {} años, Usted pertenece a la categoria de adultos".format(nombre,edad))
elif edad >= 30 and edad < 60:
    print("{}: Su edad es: {} años, Usted pertenece a la categoria adulto mayor".format(nombre,edad))
elif edad >= 60 and edad < 120:
    print("{}: Su edad es: {} años, Usted pertenece a la categoria de la tercera edad".format(nombre,edad))
else:
    print("{}: Su edad es: {} años, por lo tanto no pertenece a ninguna categoria".format(nombre,edad))

