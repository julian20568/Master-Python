#Programación orientada a objetos
#Clase: es un molde para crear mas objetos de ese tipo con
#caracteristicas parecidas

#1. definir una clas (molde para crear mas objetos de ese tipo)
#(coche) con caracteristicas similires


class Coche:
    #creamos atributos o propiedades (variables)
    #caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    #Metodos, son acciones que hace el objeto (coche) (funciones)
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
#fin definición clase

#crear objetos / instanciar la clase
coche = Coche()
print(coche.marca, coche.color) 
#llamamos los metodos que creamos 
print("Velocidad actual: ", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()#La velocidad se reduce en 1

print("Velocidad nueva: ", coche.velocidad)