import os
import random
import string
import shutil

def carpeta_Procesada(ruta_Carpeta):
    for raiz, subcarpetas, archivos in os.walk(ruta_Carpeta):
        for nombre_Carpetas in subcarpetas:
            ruta_Subcarpeta = os.path.join(raiz, nombre_Carpetas)
            nuevo_Nombre_Subcarpeta = ''.join(random.choice(string.digits) if char.isalpha() else random.choice(string.ascii_uppercase) for char in nombre_Carpetas)

            carpeta_Original = os.path.dirname(ruta_Subcarpeta)
            os.rename(ruta_Subcarpeta, os.path.join(carpeta_Original, nuevo_Nombre_Subcarpeta))
            carpeta_Procesada(os.path.join(carpeta_Original, nuevo_Nombre_Subcarpeta))
            
        for nombre_archivo in archivos:
            ruta_archivo = os.path.join(raiz, nombre_archivo)
            nombre_archivo1, extension = os.path.splitext(os.path.basename(ruta_archivo))
            nuevo_nombre_archivo2 = ''.join(random.choice(string.digits) if char.isalpha() else random.choice(string.ascii_uppercase) for char in nombre_archivo1)

            nuevo_nombre_archivo2 += extension
            carpeta_contenedora = os.path.dirname(ruta_archivo)
            nueva_ruta_Archivo = os.path.join(carpeta_contenedora, nuevo_nombre_archivo2)
            os.rename(ruta_archivo, nueva_ruta_Archivo)


ruta_Carpeta = input("Ingrese la ruta de ubicacion de la carpeta: ")

if os.path.exists(ruta_Carpeta):
    carpeta_Salida = ruta_Carpeta + '_procesado'
    shutil.copytree(ruta_Carpeta, carpeta_Salida)

    carpeta_Procesada(carpeta_Salida)
    print("Se realizo la copia")

else:
    print("No existe la ruta")
