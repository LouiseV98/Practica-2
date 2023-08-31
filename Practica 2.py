import os

ruta_Carpeta = input("Ingrese la ruta de ubicacion de la carpeta: ")
if os.path.exists(ruta_Carpeta):
    print("Si existe la ruta")
else:
    print("No existe la ruta")
