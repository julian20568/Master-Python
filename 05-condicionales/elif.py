print("#######################EJEMPLO 4#######################")

dia = int(input("Introduce el número del dia de la semana: "))

"""
if dia == 1:
    print("ES Lunes")
else:
    if dia == 2:
        print("Es Martes")
    else:
        if dia == 3:
            print("Es Miercoles")
        else:
            if dia == 4:
                print("Es Jueves")
            else:
                if dia == 5:
                    print("Es Viernes")
                else:
                        print("Es fin de semana")
"""

if dia == 1:
    print("ES Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
elif dia >= 8:
    print("Introduce un numero en un rango de 1 a 7 para validar los dias de la semana")
else:
    print("Es fin de semana")
