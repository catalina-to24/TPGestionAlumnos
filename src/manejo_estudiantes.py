import csv  # Para leer y escribir archivos CSV

# Cargar alumnos desde un archivo CSV
def cargar_alumnos(filename):
    alumnos = []
    try:
        with open(filename, 'r') as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Salta la primera línea (los títulos)
            for fila in lector:
                # Convierte las notas a números decimales
                fila[2] = float(fila[2])
                fila[3] = float(fila[3])
                fila[4] = float(fila[4])
                fila[5] = float(fila[5])
                alumnos.append(fila)
    except FileNotFoundError:
        print(f"No se encontró el archivo {filename}")
    return alumnos

# Guardar alumnos en un archivo CSV
def guardar_alumnos(filename, alumnos):
    with open(filename, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nombre", "Materia", "Nota1", "Nota2", "Nota3", "NotaFinal"])
        escritor.writerows(alumnos)

# Agregar un alumno a la lista
def agregar_alumno(alumnos, nombre, materia, nota1, nota2, nota3):
    # Verifica que las notas estén entre 0 y 10
    if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
        raise ValueError("Las notas deben estar entre 0 y 10.")
    nota_final = (nota1 + nota2 + nota3) / 3
    alumnos.append([nombre, materia, nota1, nota2, nota3, nota_final])


# Listado completo de alumnos con sus notas y promedio
def informe_listado_completo(alumnos):
    return [
        f"{a[0]} | {a[1]} | Notas: {a[2]}, {a[3]}, {a[4]} | Promedio: {a[5]:.2f}"
        for a in alumnos
    ]

# Promedio general por materia
def informe_promedio_por_materia(alumnos):
    materias = {}
    for a in alumnos:
        materia = a[1]
        if materia not in materias:
            materias[materia] = []
        materias[materia].append(a[5])
    return {m: sum(notas)/len(notas) for m, notas in materias.items()}

# Alumnos con nota final mayor a un valor dado
def informe_mayor_a(alumnos, valor):
    return [a for a in alumnos if a[5] > valor]

# Alumnos con al menos una nota menor a 4
def informe_nota_menor_a_4(alumnos):
    return [a for a in alumnos if a[2] < 4 or a[3] < 4 or a[4] < 4]

# Cantidad de aprobados y desaprobados por materia (aprobado: promedio >= 6)
def informe_aprobados_desaprobados(alumnos):
    materias = {}
    for a in alumnos:
        materia = a[1]
        if materia not in materias:
            materias[materia] = {"aprobados": 0, "desaprobados": 0}
        if a[5] >= 6:
            materias[materia]["aprobados"] += 1
        else:
            materias[materia]["desaprobados"] += 1
    return materias

# ORDENAMIENTOS

# Ordenar por nombre de alumno (A-Z)
def ordenar_por_nombre(alumnos):
    alumnos.sort(key=lambda a: a[0])

# Ordenar por nota final (de mayor a menor)
def ordenar_por_nota_final(alumnos):
    alumnos.sort(key=lambda a: a[5], reverse=True)