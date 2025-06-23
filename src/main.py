# Importar las bibliotecas necesarias
import tkinter as tk  # Biblioteca estándar para crear interfaces gráficas
from manejo_estudiantes import cargar_alumnos, guardar_alumnos, agregar_alumno  # Funciones para manejar los datos de los alumnos
from interfaz import crear_interfaz, mostrar_callback  # Funciones para crear la interfaz gráfica y mostrar datos
import os

# Definir la ruta del archivo CSV donde se almacenan los datos de los alumnos
filename = os.path.join(os.path.dirname(__file__), '../data/alumnos.csv')

# Cargar los datos de los alumnos desde el archivo CSV
students = cargar_alumnos(filename)

# Función para guardar los datos de los alumnos en el archivo CSV
def guardar_callback():
    guardar_alumnos(filename, students)

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Sistema de Gestión de Alumnos")

# Crear la interfaz gráfica, pasando los datos y las funciones necesarias
crear_interfaz(
    root,
    students,
    agregar_alumno,
    mostrar_callback,
    guardar_callback
)

# Iniciar el bucle principal de la aplicación
root.mainloop()