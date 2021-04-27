#OPERADORES LOGICOS
"""
and Y
or O
! Negación
not NO
"""


print("\n#####################EJEMPLO 5######################")

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("¿tienes edad de trabajar? Introduce tu edad: "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trajar !!")
else:
    print("No esta en edad de trabajar")

print("\n#####################EJEMPLO 6######################")

pais = "Colombia"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print("{}, Es un pais de habla hispana !!".format(pais))
else:
    print("{}, No es un pais de habla hispana :(".format(pais))

print("\n#####################EJEMPLO 7######################")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print("{}, No es un pais de habla hispana !!".format(pais))
else:
    print("{}, SI es un pais de habla hispana :(".format(pais))

print("\n#####################EJEMPLO 8######################")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print("{}, No es un pais de habla hispana !!".format(pais))
else:
    print("{}, SI es un pais de habla hispana :)".format(pais))