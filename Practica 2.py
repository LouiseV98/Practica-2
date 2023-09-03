import os
import random
import string
import shutil

def numero_Aleatorio():
    return str(random.randint(0, 9))

def letra_Aleatoria():
    return random.choice(string.ascii_uppercase)

#def replace_letters_with_random_digits(text):
    #return ''.join(random.choice(string.digits) if char.isalpha() else char for char in text)

# Función para cambiar dígitos por letras mayúsculas aleatorias
#def replace_digits_with_random_letters(text):
    #return ''.join(random.choice(string.ascii_uppercase) if char.isdigit() else char for char in text)

def procesar_Archivos(ruta_Archivo):
    with open(ruta_Archivo, 'r') as archivo:
        contenido = archivo.read()

        #contenido = replace_letters_with_random_digits(contenido)
        #contenido = replace_digits_with_random_letters(contenido)
    modificar_Contenido = ''
    for char in contenido:
        if char.isalpha():
            modificar_Contenido += numero_Aleatorio()
        elif char.isdigit():
            modificar_Contenido += letra_Aleatoria()
        else:
            modificar_Contenido += char

    #nueva_Ruta_Archivo = ruta_Archivo 
    print(modificar_Contenido)
    with open(ruta_Archivo, 'w') as nuevo_Archivo:
        nuevo_Archivo.write(modificar_Contenido)

    #with open(ruta_Archivo, 'w') as archivo:
        #archivo.write(contenido)

def carpeta_Procesada(ruta_Carpeta):
    for raiz, _, archivos in os.walk(ruta_Carpeta):
        for archivo in archivos:
            ruta_Archivos = os.path.join(raiz, archivo)
            procesar_Archivos(ruta_Archivos)

if __name__ == "__main__":
    ruta_Carpeta = input("Ingrese la ruta de ubicacion de la carpeta: ")


    if os.path.exists(ruta_Carpeta):
        carpeta_Salida = ruta_Carpeta + '_procesado'
        shutil.copytree(ruta_Carpeta, carpeta_Salida)

        carpeta_Procesada(carpeta_Salida)

    else:
        print("No existe la ruta")
