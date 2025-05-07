#para la ruta csv
from pathlib import Path 
import tkinter as tk
from manejo_estudiantes import cargar_alumnos, guardar_alumnos, agregar_alumno
from interfaz import crear_interfaz, mostrar_callback

# Obtener la ruta absoluta del directorio actual (donde está main.py)
base_dir = Path(__file__).resolve().parent

# Construir la ruta relativa al archivo CSV
filename = base_dir / "../data/alumnos.csv"

students = cargar_alumnos(filename)

def guardar_callback():
    guardar_alumnos(filename, students)

root = tk.Tk()
root.title("Sistema de Gestión de Alumnos")
crear_interfaz(root, students, agregar_alumno, mostrar_callback, guardar_callback)
root.mainloop()