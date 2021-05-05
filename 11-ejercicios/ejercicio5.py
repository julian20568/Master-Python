"""
Ejercicio 5: Crear una lista con el contenido de esta tabla:
ACCION        AVENTURA               DEPORTES
GTA            ASSINS                FIFA 21
COD            CRASH                 PRO 21
PUGB           PRINCE OF PERSIA      MOTO GP 21
"""

#crear un diccionario
tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA","COD","PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSINS","CRASH","PRINCE OF PERSIA"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for categoria in tabla:
    print(f"--------------{categoria['categoria']}--------------")
    for juegos in categoria['juegos']:
        print(juegos)