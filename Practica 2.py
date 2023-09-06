import os
import random
import string
import shutil

def procesar_Carpeta(ruta_Carpeta):
    for raiz, subcarpetas, archivos in os.walk(ruta_Carpeta):   #Iteracion para navegar entre la carpeta raiz, las subcarpetas de esta y los archivos de cada una
        for nombre_Carpetas in subcarpetas:     #Iteracion para navegar entre las subcarpetas
            ruta_Subcarpeta = os.path.join(raiz, nombre_Carpetas)   #Funcion para unir la ruta raiz y la subcarpeta
            nuevo_Nombre_Subcarpeta = ''.join(random.choice(string.digits) 
                                              if char.isalpha() else random.choice(string.ascii_uppercase) 
                                              for char in nombre_Carpetas)    #Se crea el nombre de la subcarpeta con letras y numeros aleatorios

            ruta_Carpeta_Original = os.path.dirname(ruta_Subcarpeta)    #Se verifica la ruta original de la subcarpeta
            os.rename(ruta_Subcarpeta, os.path.join(ruta_Carpeta_Original, nuevo_Nombre_Subcarpeta))    #Se reescribe el nombre de la subcarpeta uniendo la ruta de esta y el nuevo nombre creado
            procesar_Carpeta(os.path.join(ruta_Carpeta_Original, nuevo_Nombre_Subcarpeta))  #Se hace la recursividad para las siguientes subcarpetas si es que existen
            
        for nombre_Archivo in archivos: #Iteracion para navegar entre archivos
            ruta_Archivo = os.path.join(raiz, nombre_Archivo)   #Funcion para unir la ruta raiz y el archivo
            nombre_Archivo_Original, extension_Archivo = os.path.splitext(os.path.basename(ruta_Archivo))   #Funcion que devuelve el nombre del archivo tomado de la ruta de ubicacion y lo divide en el nombre y su extension
            nuevo_Nombre_Archivo = ''.join(random.choice(string.digits)   
                                           if char.isalpha() else random.choice(string.ascii_uppercase) 
                                           for char in nombre_Archivo_Original) #Se crea el nombre del archivo con letras y numeros aleatorios utilizando como arreglo los nombres de los archivos

            nuevo_Nombre_Archivo += extension_Archivo   #Se concatena el nuevo nombre del archivo y su extension original
            ruta_Carpeta_Contenedora = os.path.dirname(ruta_Archivo)    #Se vcrifica la ruta original del archivo
            nueva_Ruta_Archivo = os.path.join(ruta_Carpeta_Contenedora, nuevo_Nombre_Archivo)   #Funcion para unir la ruta original del archivo y su nuevo nombre creado
            os.rename(ruta_Archivo, nueva_Ruta_Archivo) #Se reescribe el nombre del archivo utilizando la ruta obtenida 


ruta_Carpeta_Raiz = input("Ingrese la ruta de ubicacion de la carpeta: ") #Entrada para la ruta de ubicacion de la carpeta

if os.path.exists(ruta_Carpeta_Raiz):
    ruta_Carpeta_Salida = ruta_Carpeta_Raiz + '_procesado' #Crea una ruta la cual llevara a una carpeta diferente a la raiz con una palabra concatenada
    shutil.copytree(ruta_Carpeta_Raiz, ruta_Carpeta_Salida) #Funcion de la libreria shutil que hace una copia del archivo otorgandole la ruta de ubicacion

    procesar_Carpeta(ruta_Carpeta_Salida) #Llamada a la funcion la cual pasa como parametro la ruta de ubicacion de la carpeta raiz
    print("Se realizo la copia")

else: #Validacion para la entrada de datos 
    print("No existe la ruta")
