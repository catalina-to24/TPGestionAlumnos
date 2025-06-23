import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import manejo_estudiantes

def crear_interfaz(root, students, agregar_callback, mostrar_callback, guardar_callback):
    # Sección para agregar alumnos
    frame_add = tk.Frame(root)
    frame_add.pack(pady=10)

    tk.Label(frame_add, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(frame_add)
    entry_nombre.grid(row=0, column=1)

    tk.Label(frame_add, text="Materia:").grid(row=1, column=0)
    entry_materia = tk.Entry(frame_add)
    entry_materia.grid(row=1, column=1)

    tk.Label(frame_add, text="Nota 1:").grid(row=2, column=0)
    entry_nota1 = tk.Entry(frame_add)
    entry_nota1.grid(row=2, column=1)

    tk.Label(frame_add, text="Nota 2:").grid(row=3, column=0)
    entry_nota2 = tk.Entry(frame_add)
    entry_nota2.grid(row=3, column=1)

    tk.Label(frame_add, text="Nota 3:").grid(row=4, column=0)
    entry_nota3 = tk.Entry(frame_add)
    entry_nota3.grid(row=4, column=1)

    def agregar_alumno_gui():
        try:
            nombre = entry_nombre.get()
            materia = entry_materia.get()
            nota1 = float(entry_nota1.get())
            nota2 = float(entry_nota2.get())
            nota3 = float(entry_nota3.get())
            agregar_callback(students, nombre, materia, nota1, nota2, nota3)
            entry_nombre.delete(0, tk.END)
            entry_materia.delete(0, tk.END)
            entry_nota1.delete(0, tk.END)
            entry_nota2.delete(0, tk.END)
            entry_nota3.delete(0, tk.END)
            mostrar_callback(tree, students)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa números válidos para las notas (0 a 10).")

    tk.Button(frame_add, text="Agregar Alumno", command=agregar_alumno_gui).grid(row=5, column=0, columnspan=2, pady=10)

    # Tabla para mostrar alumnos e informes
    frame_list = tk.Frame(root)
    frame_list.pack(pady=10)

    tree = ttk.Treeview(frame_list, columns=("Nombre", "Materia", "Nota1", "Nota2", "Nota3", "NotaFinal"), show="headings")
    for col in ("Nombre", "Materia", "Nota1", "Nota2", "Nota3", "NotaFinal"):
        tree.heading(col, text=col)
    tree.pack()

    # -------- INFORMES EN LA TABLA --------
    def mostrar_informe_listado():
        mostrar_callback(tree, students)

    def mostrar_informe_promedio_materia():
        for item in tree.get_children():
            tree.delete(item)
        promedios = manejo_estudiantes.informe_promedio_por_materia(students)
        for materia, prom in promedios.items():
            tree.insert("", "end", values=("", materia, "", "", "", f"{prom:.2f}"))

    def mostrar_informe_mayor_a():
        valor = simpledialog.askfloat("Nota mínima", "Mostrar alumnos con nota final mayor a:")
        if valor is not None:
            for item in tree.get_children():
                tree.delete(item)
            resultado = manejo_estudiantes.informe_mayor_a(students, valor)
            for alumno in resultado:
                tree.insert("", "end", values=(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], f"{alumno[5]:.2f}"))

    def mostrar_informe_menor_4():
        for item in tree.get_children():
            tree.delete(item)
        resultado = manejo_estudiantes.informe_nota_menor_a_4(students)
        for alumno in resultado:
            tree.insert("", "end", values=(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], f"{alumno[5]:.2f}"))

    def mostrar_informe_aprobados():
        for item in tree.get_children():
            tree.delete(item)
        resultado = manejo_estudiantes.informe_aprobados_desaprobados(students)
        for materia, info in resultado.items():
            tree.insert("", "end", values=("", materia, "", "", f"Aprob: {info['aprobados']}", f"Desap: {info['desaprobados']}"))

    # -------- BOTONES --------
    tk.Button(root, text="Listado completo", command=mostrar_informe_listado).pack(pady=2)
    tk.Button(root, text="Promedio por materia", command=mostrar_informe_promedio_materia).pack(pady=2)
    tk.Button(root, text="Alumnos con nota final mayor a...", command=mostrar_informe_mayor_a).pack(pady=2)
    tk.Button(root, text="Alumnos con alguna nota menor a 4", command=mostrar_informe_menor_4).pack(pady=2)
    tk.Button(root, text="Aprobados y desaprobados por materia", command=mostrar_informe_aprobados).pack(pady=2)

    # -------- ORDENAMIENTOS --------
    def ordenar_nombre():
        manejo_estudiantes.ordenar_por_nombre(students)
        mostrar_callback(tree, students)

    def ordenar_nota_final():
        manejo_estudiantes.ordenar_por_nota_final(students)
        mostrar_callback(tree, students)

    tk.Button(root, text="Ordenar por nombre", command=ordenar_nombre).pack(pady=2)
    tk.Button(root, text="Ordenar por nota final", command=ordenar_nota_final).pack(pady=2)

    # Botón para guardar y salir
    tk.Button(root, text="Guardar y Salir", command=lambda: [guardar_callback(), root.destroy()]).pack(pady=10)

def mostrar_callback(tree, students):
    # Borra la tabla
    for item in tree.get_children():
        tree.delete(item)
    # Muestra todos los alumnos en la tabla
    for alumno in students:
        tree.insert("", "end", values=(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], f"{alumno[5]:.2f}"))