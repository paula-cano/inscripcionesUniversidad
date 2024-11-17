from src.baseDeDatos.GestorBaseDatos import GestorBaseDatos
from tkinter import filedialog
import tkinter as tk
import os

class InterfazConsola:
    def __init__(self):
        # Inicializamos una instancia de tk pero la mantenemos oculta
        self.root = tk.Tk()
        self.root.withdraw()
        self.gestor_db = GestorBaseDatos()

    def mostrarMenu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Cargar archivo de inscripciones")
            print("2. Mostrar total de materias por estudiante")
            print("3. Filtrar estudiantes por materia")
            print("4. Exportar datos a JSON/CSV")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.cargarArchivo()
            elif opcion == "2":
                self.mostrarEstudiantes()
            elif opcion == "3":
                self.filtrarPorMateria()
            elif opcion == "4":
                self.exportarDatos()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    def cargarArchivo(self):
        try:
            # Abre el diálogo para seleccionar archivos
            ruta = filedialog.askopenfilename(
                title="Seleccionar archivo de inscripciones",
                filetypes=[
                    ("Archivos CSV", "*.csv"),
                    ("Archivos de texto", "*.txt"),
                    ("Todos los archivos", "*.*")
                ]
            )
            
            # Verifica si se seleccionó un archivo
            if ruta:
                self.gestor_db.procesar_archivo(ruta)
                print(f"Archivo seleccionado: {os.path.basename(ruta)}")
                print("Archivo procesado exitosamente.")
            else:
                print("No se seleccionó ningún archivo.")
                
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

