import csv  # Biblioteca para manejar archivos CSV
from pathlib import Path  # Biblioteca para manejar rutas de archivos de forma flexible

# Función para cargar los datos de los alumnos desde un archivo CSV
def cargar_alumnos(filename):
    """
    Lee los datos de un archivo CSV y los carga en una lista.
    Cada fila del archivo representa un alumno con sus datos.
    """
    students = []  # Lista para almacenar los datos de los alumnos
    try:
        with open(filename, 'r') as file:  # Abrir el archivo en modo lectura
            reader = csv.reader(file)  # Crear un lector CSV
            next(reader)  # Saltar la cabecera del archivo
            for row in reader:
                row[2:6] = list(map(float, row[2:6]))  # Convertir las notas (columnas 2 a 5) a tipo float
                students.append(row)  # Agregar la fila procesada a la lista de alumnos
    except FileNotFoundError:
        # Lanzar un error si el archivo no existe
        raise FileNotFoundError(f"El archivo {filename} no existe. Verifica la ruta.")
    return students  # Devolver la lista de alumnos

# Función para guardar los datos de los alumnos en un archivo CSV
def guardar_alumnos(filename, students):
    """
    Escribe los datos de los alumnos en un archivo CSV.
    Sobrescribe el archivo si ya existe.
    """
    with open(filename, 'w', newline='') as file:  # Abrir el archivo en modo escritura
        writer = csv.writer(file)  # Crear un escritor CSV
        # Escribir la cabecera del archivo
        writer.writerow(["Nombre", "Materia", "Nota1", "Nota2", "Nota3", "NotaFinal"])
        # Escribir los datos de los alumnos
        writer.writerows(students)

# Función para agregar un nuevo alumno a la lista
def agregar_alumno(students, nombre, materia, nota1, nota2, nota3):
    """
    Agrega un nuevo alumno a la lista de estudiantes.
    Calcula la nota final como el promedio de las tres notas.
    """
    # Validar que las notas estén en el rango de 0 a 10
    if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
        raise ValueError("Las notas deben estar entre 0 y 10.")
    # Calcular la nota final como el promedio de las tres notas
    nota_final = (nota1 + nota2 + nota3) / 3
    # Agregar el nuevo alumno a la lista
    students.append([nombre, materia, nota1, nota2, nota3, nota_final])

# Función para mostrar los datos de los alumnos en la consola
def mostrar_alumnos(students):
    """
    Imprime los datos de los alumnos en la consola.
    Incluye el nombre, materia, notas y promedio final.
    """
    for student in students:
        # Formatear e imprimir los datos de cada alumno
        print(f"{student[0]} - {student[1]} - Notas: {student[2]}, {student[3]}, {student[4]} - Promedio: {student[5]:.2f}")