import csv
from pathlib import Path

def cargar_alumnos(filename):
    
    students = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la cabecera
            for row in reader:
                row[2:6] = list(map(float, row[2:6]))  # Convertir notas a float
                students.append(row)
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {filename} no existe. Verifica la ruta.")
    return students

def guardar_alumnos(filename, students):
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Materia", "Nota1", "Nota2", "Nota3", "NotaFinal"])
        writer.writerows(students)

def agregar_alumno(students, nombre, materia, nota1, nota2, nota3):
    
    if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
        raise ValueError("Las notas deben estar entre 0 y 10.")
    nota_final = (nota1 + nota2 + nota3) / 3
    students.append([nombre, materia, nota1, nota2, nota3, nota_final])

def mostrar_alumnos(students):
    
    for student in students:
        print(f"{student[0]} - {student[1]} - Notas: {student[2]}, {student[3]}, {student[4]} - Promedio: {student[5]:.2f}")