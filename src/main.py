import tkinter as tk
from manejo_estudiantes import cargar_alumnos, guardar_alumnos, agregar_alumno, mostrar_alumnos
from interfaz import crear_interfaz

filename = "c:\\Users\\Administrator\\OneDrive\\Desktop\\UADE\\1° año\\1°Cuatri\\Intro_algoritmia\\TP\\sistemas-alumnos\\data\\alumnos.csv"
students = cargar_alumnos(filename)

def guardar_callback():
    guardar_alumnos(filename, students)

root = tk.Tk()
root.title("Sistema de Gestión de Alumnos")
crear_interfaz(root, students, agregar_alumno, mostrar_alumnos, guardar_callback)
root.mainloop()