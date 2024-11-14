# src/consolidado.py

from src.programa.archivo import LectorArchivoTexto
from src.baseDeDatos.controladorBD import GestorBaseDatos
from src.modelos.estudiante import Estudiante

class ConsolidadoInscripciones:
    def __init__(self):
        self.estudiantes = []  # Listado de objetos Estudiante
        self.lector = LectorArchivoTexto()
        self.base_datos = GestorBaseDatos()

    def consolidar_archivo(self, ruta: str):
        lineas = self.lector.obtener_lineas(ruta)
        for linea in lineas:
            if self.validar_datos_linea(linea):
                self.procesar_linea(linea)

    def procesar_linea(self, linea: str):
        # Procesa cada línea y la convierte en un objeto Estudiante y Materia
        cedula, nombre, codigo_materia, nombre_materia = linea.split(",")
        estudiante = self.buscar_estudiante(cedula)
        if not estudiante:
            estudiante = Estudiante(cedula, nombre)
            self.estudiantes.append(estudiante)
        estudiante.adicionar_materia(codigo_materia, nombre_materia)

    def buscar_estudiante(self, cedula: str):
        # Busca un estudiante por su cédula en la lista de estudiantes
        return next((est for est in self.estudiantes if est.cedula == cedula), None)

    def validar_datos_linea(self, linea: str):
        # Llama al validador de LectorArchivoTexto para validar el formato
        return self.lector.validador.validar_formato_linea(linea)

    def obtener_estudiantes_por_materia(self, codigo_materia: str):
        # Devuelve una lista de estudiantes inscritos en una materia específica
        return [est for est in self.estudiantes if any(mat.codigo == codigo_materia for mat in est.materias)]

    def get_total_materias_estudiante(self, cedula: str):
        estudiante = self.buscar_estudiante(cedula)
        return estudiante.get_total_materias() if estudiante else 0
