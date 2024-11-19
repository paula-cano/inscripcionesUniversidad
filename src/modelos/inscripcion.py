from src.baseDeDatos.GestorBaseDatos import GestorBaseDatos
from src.baseDeDatos.validador import ValidadorDatos
import sqlite3

class ConsolidadoInscripciones:
    def __init__(self):
        self.base_datos = GestorBaseDatos()
        self.validador = ValidadorDatos()
        self.base_datos.conectar()

    def Consolidar_archivo(self, ruta_archivo: str):
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    if not self.validador.validar_formato_linea(linea):
                        print(f"Línea inválida ignorada: {linea.strip()}")
                        continue
                    cedula, nombre_estudiante, codigo_materia, nombre_materia = linea.strip().split(",")

                    if not self.verificar_estudiante_creado(cedula):
                        self.base_datos.guardar_estudiante(cedula,nombre_estudiante)
                    if not self.verificar_materia_creada(codigo_materia):
                        self.base_datos.guardar_materia(codigo_materia, nombre_materia)
                    self.base_datos.guardar_inscripcion(cedula, codigo_materia)   
            print("Datos procesados y guardados en la base de datos.")
        except FileNotFoundError:
                    print(f"Error: No se encontró el archivo '{ruta_archivo}'.")
        except sqlite3.Error as e:
            print(f"Error con la base de datos: {e}")
        except Exception as e:
            print(f"Error inesperado al procesar el archivo: {e}")

    def verificar_estudiante_creado(self, cedula: str) -> bool:
        return self.base_datos.obtener_estudiante(cedula) is not None

    def verificar_materia_creada(self, codigo_materia: str) -> bool:
        return self.base_datos.obtener_materia(codigo_materia) is not None
    
    def mostrar_materias_por_estudiante(self, cedula: str):
        materias = self.base_datos.obtener_materias_por_estudiante(cedula)
        if materias:
            print(f"Materias inscritas para el estudiante {cedula}:")
            for codigo, nombre in materias:
                print(f"- {codigo}: {nombre}")
        else:
            print(f"No se encontraron materias para el estudiante {cedula}.")
            
    def mostrar_estudiantes_por_materia(self, codigo_materia: str):
        estudiantes = self.base_datos.obtener_estudiantes_por_materia(codigo_materia)
        if estudiantes:
            print(f"Estudiantes inscritos en la materia {codigo_materia}:")
            for cedula, nombre in estudiantes:
                print(f"- {cedula}: {nombre}")
        else:
            print(f"No se encontraron estudiantes para la materia {codigo_materia}.")
            
    def total_materias_estudiante(self, cedula: str):
        total = self.base_datos.obtener_total_materias_estudiante(cedula)
        print(f"Total de materias inscritas para el estudiante {cedula}: {total}")
        
    def desconectarDB(self):
        self.base_datos.desconectar()

