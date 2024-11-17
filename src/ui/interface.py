from src.modelos.inscripcion import ConsolidadoInscripciones
from src.baseDeDatos.GestorBaseDatos import GestorBaseDatos
from tkinter import filedialog
import tkinter as tk
import os

class InterfazConsola:
    def __init__(self):
        # Inicializamos una instancia de tk pero la mantenemos oculta
        self.root = tk.Tk()
        self.root.withdraw()
        self.inscripciones = ConsolidadoInscripciones()

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
                self.mostrar_total_materias_estudiante()
            elif opcion == "3":
                self.filtrarPorMateria()
            elif opcion == "4":
                self.exportarDatos()
            elif opcion == "5":
                self.inscripciones.desconectarDB()
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
                print(f"Archivo seleccionado: {os.path.basename(ruta)}")
                self.inscripciones.consolidar_archivo(ruta)
                print("Archivo procesado exitosamente.")
            else:
                print("No se seleccionó ningún archivo.")
                
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def mostrar_total_materias_estudiante(self):
        try:
            cedula = input("Ingrese la cédula del estudiante: ").strip()
            materias = self.inscripciones.total_materias_estudiante(cedula)
            if materias:
                print(f"\nEl total de materias inscritas para el estudiante {cedula} es: {materias}")
            else:
                print(f"No se encontraron materias para el estudiante {cedula}.")
        except Exception as e:
            print(f"Error al mostrar las materias del estudiante: {e}")
            
    def filtrarPorMateria(self):
        try:
            codigo_materia = input("Ingrese el código de la materia: ").strip()
            estudiantes = self.inscripciones.mostrar_estudiantes_por_materia(codigo_materia)
            if estudiantes:
                print(f"\nEstudiantes inscritos en la materia {codigo_materia}:")
                for estudiante in estudiantes:
                    print(f"- {estudiante['cedula']}: {estudiante['nombre']}")
            else:
                print(f"No se encontraron estudiantes para la materia {codigo_materia}.")
        except Exception as e:
            print(f"Error al filtrar estudiantes por materia: {e}")
            
    def exportarDatos(self):
        try:
            # Implementa la lógica para exportar datos a JSON o CSV
            print("Exportar datos aún no está implementado.")
        except Exception as e:
            print(f"Error al exportar los datos: {e}")
            
    