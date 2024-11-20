from src.modelos.inscripcion import ConsolidadoInscripciones
from tkinter import filedialog
import tkinter as tk
import os
import csv

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
                self.exportar_tabla()
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
                    ("Archivos de texto", "*.txt")
                ]
            )
            
            # Verifica si se seleccionó un archivo
            if ruta:
                print(f"Archivo seleccionado: {os.path.basename(ruta)}")
                self.inscripciones.Consolidar_archivo(ruta)
                print("Archivo procesado exitosamente.")
            else:
                print("No se seleccionó ningún archivo.")
                
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def mostrar_total_materias_estudiante(self):
        try:
            cedula = input("Ingrese la cédula del estudiante: ").strip()
            self.inscripciones.total_materias_estudiante(cedula)
        except Exception as e:
            print(f"Error al mostrar las materias del estudiante: {e}")
            
    def filtrarPorMateria(self):
        try:
            codigo_materia = input("Ingrese el código de la materia: ").strip()
            self.inscripciones.mostrar_estudiantes_por_materia(codigo_materia)                
        except Exception as e:
            print(f"Error al filtrar estudiantes por materia: {e}")
            
    def exportar_tabla(self):
        #Permite exportar una tabla de la base de datos a un archivo .csv o .txt.
        try:
            nombre_tabla = input("Ingrese el nombre de la tabla a exportar: ").strip()
            columnas, filas = self.inscripciones.exportar_tabla(nombre_tabla)

            if not columnas or not filas:
                print(f"No se encontraron datos en la tabla '{nombre_tabla}'.")
                return

            # Abrir ventana de guardado
            ruta_guardado = filedialog.asksaveasfilename(
                title=f"Guardar {nombre_tabla}",
                defaultextension=".csv",
                filetypes=[("Archivo CSV", "*.csv"), ("Archivo JSON", "*.json")]
            )

            if not ruta_guardado:
                print("No se seleccionó ninguna ubicación para guardar.")
                return

            # Guardar los datos en el archivo
            if ruta_guardado.endswith(".csv"):
                self.guardar_csv(ruta_guardado, columnas, filas)
            elif ruta_guardado.endswith(".json"):
                self.guardar_json(ruta_guardado, columnas, filas)
            else:
                print("Formato de archivo no soportado.")
                return

            print(f"Datos exportados exitosamente a {ruta_guardado}")

        except Exception as e:
            print(f"Error al exportar la tabla: {e}")
            
    def guardar_csv(self, ruta: str, columnas: list, filas: list):
        #Guarda los datos en un archivo CSV.
        """
        :param ruta: Ruta del archivo CSV.
        :param columnas: Lista de nombres de las columnas.
        :param filas: Lista de filas (datos de la tabla).
        """
        try:
            with open(ruta, "w", newline="", encoding="utf-8") as archivo_csv:
                escritor = csv.writer(archivo_csv)
                escritor.writerow(columnas)  # Escribir encabezados
                escritor.writerows(filas)   # Escribir filas
        except Exception as e:
            print(f"Error al guardar el archivo CSV: {e}")

    def guardar_json(self, ruta: str, columnas: list, filas: list):   
        #Guarda los datos en un archivo JSON.
        """
        :param ruta: Ruta del archivo JSON.
        :param columnas: Lista de nombres de las columnas.
        :param filas: Lista de filas (datos de la tabla).
        """
        try:
            datos = [dict(zip(columnas, fila)) for fila in filas]
            with open(ruta, "w", encoding="utf-8") as archivo_json:
                import json
                json.dump(datos, archivo_json, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar el archivo JSON: {e}")


            
    