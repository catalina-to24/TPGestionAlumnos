import tkinter as tk  # Biblioteca estándar para crear interfaces gráficas
from tkinter import messagebox, ttk  # messagebox para mensajes emergentes, ttk para widgets avanzados como tablas

# Función principal para crear la interfaz gráfica
def crear_interfaz(root, students, agregar_callback, mostrar_callback, guardar_callback):
    # Frame para agregar alumnos (contenedor para los campos de entrada y el botón de agregar)
    frame_add = tk.Frame(root)
    frame_add.pack(pady=10)  # Margen vertical de 10 píxeles

    # Etiqueta y campo de entrada para el nombre del alumno
    tk.Label(frame_add, text="Nombre:").grid(row=0, column=0)  # Etiqueta en la fila 0, columna 0
    entry_nombre = tk.Entry(frame_add)  # Campo de texto para ingresar el nombre
    entry_nombre.grid(row=0, column=1)  # Campo en la fila 0, columna 1

    # Etiqueta y campo de entrada para la materia
    tk.Label(frame_add, text="Materia:").grid(row=1, column=0)  # Etiqueta en la fila 1, columna 0
    entry_materia = tk.Entry(frame_add)  # Campo de texto para ingresar la materia
    entry_materia.grid(row=1, column=1)  # Campo en la fila 1, columna 1

    # Etiqueta y campo de entrada para la Nota 1
    tk.Label(frame_add, text="Nota 1:").grid(row=2, column=0)  # Etiqueta en la fila 2, columna 0
    entry_nota1 = tk.Entry(frame_add)  # Campo de texto para ingresar la Nota 1
    entry_nota1.grid(row=2, column=1)  # Campo en la fila 2, columna 1

    # Etiqueta y campo de entrada para la Nota 2
    tk.Label(frame_add, text="Nota 2:").grid(row=3, column=0)  # Etiqueta en la fila 3, columna 0
    entry_nota2 = tk.Entry(frame_add)  # Campo de texto para ingresar la Nota 2
    entry_nota2.grid(row=3, column=1)  # Campo en la fila 3, columna 1

    # Etiqueta y campo de entrada para la Nota 3
    tk.Label(frame_add, text="Nota 3:").grid(row=4, column=0)  # Etiqueta en la fila 4, columna 0
    entry_nota3 = tk.Entry(frame_add)  # Campo de texto para ingresar la Nota 3
    entry_nota3.grid(row=4, column=1)  # Campo en la fila 4, columna 1

    # Función para agregar un alumno desde la interfaz gráfica
    def agregar_alumno_gui():
        try:
            # Obtener los valores ingresados por el usuario
            nombre = entry_nombre.get()  # Obtener el texto del campo "Nombre"
            materia = entry_materia.get()  # Obtener el texto del campo "Materia"
            nota1 = float(entry_nota1.get())  # Convertir el texto de "Nota 1" a número decimal
            nota2 = float(entry_nota2.get())  # Convertir el texto de "Nota 2" a número decimal
            nota3 = float(entry_nota3.get())  # Convertir el texto de "Nota 3" a número decimal

            # Llamar a la función de callback para agregar el alumno a la lista
            agregar_callback(students, nombre, materia, nota1, nota2, nota3)

            # Mostrar un mensaje de éxito
            messagebox.showinfo("Éxito", "Alumno agregado exitosamente.")

            # Limpiar los campos de entrada
            entry_nombre.delete(0, tk.END)
            entry_materia.delete(0, tk.END)
            entry_nota1.delete(0, tk.END)
            entry_nota2.delete(0, tk.END)
            entry_nota3.delete(0, tk.END)
        except ValueError as e:
            # Mostrar un mensaje de error si ocurre un problema (por ejemplo, si las notas no son números)
            messagebox.showerror("Error", str(e))

    # Botón para agregar un alumno
    tk.Button(frame_add, text="Agregar Alumno", command=agregar_alumno_gui).grid(row=5, column=0, columnspan=2, pady=10)

    # Frame para mostrar alumnos (contenedor para la tabla)
    frame_list = tk.Frame(root)
    frame_list.pack(pady=10)  # Margen vertical de 10 píxeles

    # Tabla para mostrar los datos de los alumnos
    tree = ttk.Treeview(frame_list, columns=("Nombre", "Materia", "Nota1", "Nota2", "Nota3", "NotaFinal"), show="headings")
    tree.heading("Nombre", text="Nombre")  # Encabezado de la columna "Nombre"
    tree.heading("Materia", text="Materia")  # Encabezado de la columna "Materia"
    tree.heading("Nota1", text="Nota 1")  # Encabezado de la columna "Nota 1"
    tree.heading("Nota2", text="Nota 2")  # Encabezado de la columna "Nota 2"
    tree.heading("Nota3", text="Nota 3")  # Encabezado de la columna "Nota 3"
    tree.heading("NotaFinal", text="Nota Final")  # Encabezado de la columna "Nota Final"
    tree.pack()  # Colocar la tabla en la ventana

    # Botón para mostrar los alumnos en la tabla
    tk.Button(root, text="Mostrar Alumnos", command=lambda: mostrar_callback(tree, students)).pack(pady=10)

    # Botón para guardar los datos y salir de la aplicación
    tk.Button(root, text="Guardar y Salir", command=lambda: [guardar_callback(), root.destroy()]).pack(pady=10)

# Función para mostrar los alumnos en la tabla
def mostrar_callback(tree, students):
    # Limpiar el Treeview antes de agregar nuevos datos
    for item in tree.get_children():
        tree.delete(item)

    # Agregar los datos de los alumnos al Treeview
    for student in students:
        tree.insert("", "end", values=(student[0], student[1], student[2], student[3], student[4], student[5]))