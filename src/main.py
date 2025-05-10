# Importar las bibliotecas necesarias
from pathlib import Path  # Para manejar rutas de archivos de forma flexible y multiplataforma
import tkinter as tk  # Biblioteca estándar para crear interfaces gráficas
from manejo_estudiantes import cargar_alumnos, guardar_alumnos, agregar_alumno  # Funciones para manejar los datos de los alumnos
from interfaz import crear_interfaz, mostrar_callback  # Funciones para crear la interfaz gráfica y mostrar datos

# Obtener la ruta absoluta del directorio actual (donde está ubicado este archivo main.py)
base_dir = Path(__file__).resolve().parent

# Construir la ruta relativa al archivo CSV donde se almacenan los datos de los alumnos
filename = base_dir / "../data/alumnos.csv"  # Ruta relativa al archivo "alumnos.csv" dentro de la carpeta "data"

# Cargar los datos de los alumnos desde el archivo CSV
students = cargar_alumnos(filename)  # La función devuelve una lista con los datos de los alumnos

# Función para guardar los datos de los alumnos en el archivo CSV
def guardar_callback():
    guardar_alumnos(filename, students)  # Llama a la función que guarda los datos en el archivo CSV

# Crear la ventana principal de la aplicación
root = tk.Tk()  # Inicializa la ventana principal de tkinter
root.title("Sistema de Gestión de Alumnos")  # Establece el título de la ventana

# Crear la interfaz gráfica, pasando los datos y las funciones necesarias
crear_interfaz(
    root,  # Ventana principal
    students,  # Lista de alumnos cargada desde el archivo
    agregar_alumno,  # Función para agregar un alumno a la lista
    mostrar_callback,  # Función para mostrar los alumnos en la tabla
    guardar_callback  # Función para guardar los datos en el archivo
)

# Iniciar el bucle principal de la aplicación (mantiene la ventana abierta)
root.mainloop()