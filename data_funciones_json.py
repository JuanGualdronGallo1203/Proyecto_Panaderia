import json  # Importa el módulo JSON para manejar archivos JSON.
import os  # Importa el módulo OS para verificar la existencia de archivos.
from datetime import datetime  # Importa el módulo datetime para generar códigos únicos basados en la fecha y hora.

# Define el nombre del archivo JSON que almacenará los datos de productos.
ARCHIVO_PRODUCTOS = "productos.json"
ARCHIVO_PEDIDOS = "pedidos.json"

def cargar_datos(archivo):
    """
    Carga datos desde un archivo JSON.
    Si el archivo no existe, devuelve un diccionario vacío.
    """
    if os.path.exists(archivo):  # Verifica si el archivo existe.
        with open(archivo, 'r') as f:  # Abre el archivo en modo lectura ('r').
            return json.load(f)  # Carga los datos del archivo JSON y los devuelve como un diccionario.
    return {}  # Si el archivo no existe, devuelve un diccionario vacío.

def guardar_datos(datos, archivo):
    """
    Guarda datos en un archivo JSON.
    """
    with open(archivo, 'w') as f:  # Abre el archivo en modo escritura ('w').
        json.dump(datos, f, indent=4)  # Guarda los datos en formato JSON con sangría para mejorar la legibilidad.

def generar_codigo():
    """
    Genera un código único basado en la fecha y hora actual.
    Formato: YYYYMMDDHHMMSS (año, mes, día, hora, minuto, segundo).
    """
    return datetime.now().strftime('%Y%m%d%H%M%S')  # Retorna la fecha y hora actual formateada como un string.