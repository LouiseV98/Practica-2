import os
import random
import string
import shutil

def numero_Aleatorio():
    return str(random.randint(0,9))

def letra_Aleatoria():
    return random.choice(string.ascii_uppercase)

ruta_Carpeta = input("Ingrese la ruta de ubicacion de la carpeta: ")
if os.path.exists(ruta_Carpeta):
    carpeta_Salida = ruta_Carpeta + '_procesado'
    shutil.copytree(ruta_Carpeta, carpeta_Salida)
else:
    print("No existe la ruta")
