#IFs anidados
print("#####################EJEMPLO 2######################")
nombre = "Julián Obando"
ciudad = "Colombia"
continente = "Suramerica"
edad = 27
mayoria_edad = 18

if edad >= mayoria_edad:
    print("{}, es mayor de edad".format(nombre))

    if continente != "Suramerica":
        print("El usuario no es de Surameriano".format(ciudad))
    else:
        print("Es Suramericano y es de, {}".format(ciudad))
else:
    print("{}, no es mayor de edad".format(nombre))