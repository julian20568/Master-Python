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
    #Getters y Setters
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo
    
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
#fin definición clase

#crear objetos / instanciar la clase
coche = Coche()

print("COCHE 1:")

coche.setColor("amarillo")
coche.setModelo("Murcielago")


print(coche.marca, coche.getModelo(), coche.getColor()) 
#llamamos los metodos que creamos 
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()#La velocidad se reduce en 1

print("Velocidad nueva: ", coche.getVelocidad())

print("---------------------")

#Crear mas objetos 
coche2 = Coche()

coche2.setColor("verde")
coche2.setModelo("Gallardo")

print("COCHE 2:")
print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))
