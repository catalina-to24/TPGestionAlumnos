import tkinter as tk
from tkinter import messagebox, ttk

def crear_interfaz(root, students, agregar_callback, mostrar_callback, guardar_callback):
    # Frame para agregar alumnos
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
            messagebox.showinfo("Éxito", "Alumno agregado exitosamente.")
            entry_nombre.delete(0, tk.END)
            entry_materia.delete(0, tk.END)
            entry_nota1.delete(0, tk.END)
            entry_nota2.delete(0, tk.END)
            entry_nota3.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    tk.Button(frame_add, text="Agregar Alumno", command=agregar_alumno_gui).grid(row=5, column=0, columnspan=2, pady=10)

    # Frame para mostrar alumnos
    frame_list = tk.Frame(root)
    frame_list.pack(pady=10)

    tree = ttk.Treeview(frame_list, columns=("Nombre", "Materia", "Nota1", "Nota2", "Nota3", "NotaFinal"), show="headings")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Materia", text="Materia")
    tree.heading("Nota1", text="Nota 1")
    tree.heading("Nota2", text="Nota 2")
    tree.heading("Nota3", text="Nota 3")
    tree.heading("NotaFinal", text="Nota Final")
    tree.pack()

    tk.Button(root, text="Mostrar Alumnos", command=lambda: mostrar_callback(tree, students)).pack(pady=10)
    tk.Button(root, text="Guardar y Salir", command=lambda: [guardar_callback(), root.destroy()]).pack(pady=10)