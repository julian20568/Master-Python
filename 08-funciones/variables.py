"""
Variables locales: se definen dentro de la funciòn y no
se puede usar dentro de ella, solo estan disponibles dentro.
A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una funcion 
y estan disponibles dentro y fuera de ellas.
"""

# variable global

frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holaMundo():
    frase = "Hola mundo" #variable local
    print("Dentro de la funcion")
    print(frase)

    year = 2021
    print(year)

    global website
    website = "julianobando.web"
    print("DENTRO:", website)

    return "Datos devuelto" + str(year)

#holaMundo() 
print(holaMundo())
print("FUERA", website)