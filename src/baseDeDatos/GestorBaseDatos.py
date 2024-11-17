# src/baseDeDatos/GestorBaseDatos.py

import sqlite3
from src.programa.archivo import LectorArchivoTexto
from src.programa.validador import ValidadorDatos
from src.modelos.estudiante import Estudiante
from src.modelos.materia import Materia

class GestorBaseDatos:
    def __init__(self, url_db='inscripciones.db'):
        self.URL_DB = url_db
        self.conexion = None
        self.lector = LectorArchivoTexto()
        self.validador = ValidadorDatos()

    def conectar(self):
        try:
            self.conexion = sqlite3.connect(self.URL_DB)
            self.inicializar_tablas()
            print("Conexión establecida con la base de datos.")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise

    def desconectar(self):
        if self.conexion:
            try:
                self.conexion.close()
                print("Conexión cerrada con la base de datos.")
            except sqlite3.Error as e:
                print(f"Error al cerrar la conexión: {e}")

    def inicializar_tablas(self):
        """Crea las tablas necesarias si no existen"""
        cursor = self.conexion.cursor()
        try:
            # Tabla Estudiantes
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS estudiantes (
                    cedula TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL
                )
            ''')
            
            # Tabla Materias
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS materias (
                    codigo TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL
                )
            ''')
            
            # Tabla Inscripciones
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS inscripciones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cedula_estudiante TEXT,
                    codigo_materia TEXT,
                    FOREIGN KEY (cedula_estudiante) REFERENCES estudiantes(cedula),
                    FOREIGN KEY (codigo_materia) REFERENCES materias(codigo),
                    UNIQUE(cedula_estudiante, codigo_materia)
                )
            ''')
            
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al crear las tablas: {e}")
            raise

    def procesar_archivo(self, ruta_archivo: str):
        """Procesa un archivo y guarda sus datos en la base de datos"""
        try:
            self.conectar()
            lineas = self.lector.obtener_lineas(ruta_archivo)
            estudiantes_procesados = {}

            for linea in lineas:
                linea = linea.strip()
                if not linea:
                    continue

                if not self.validador.validar_formato_linea(linea):
                    print(f"Línea inválida ignorada: {linea}")
                    continue

                cedula, nombre, codigo_materia, nombre_materia = linea.split(",")

                # Crear o recuperar estudiante
                if cedula not in estudiantes_procesados:
                    estudiantes_procesados[cedula] = Estudiante(cedula, nombre)
                
                # Adicionar materia al estudiante
                estudiantes_procesados[cedula].adicionar_materia(codigo_materia, nombre_materia)

            # Guardar todos los estudiantes procesados
            for estudiante in estudiantes_procesados.values():
                self.guardar_estudiante_completo(estudiante)

            print(f"Archivo procesado exitosamente. {len(estudiantes_procesados)} estudiantes procesados.")

        except Exception as e:
            print(f"Error al procesar el archivo: {e}")
            raise
        finally:
            self.desconectar()

    def guardar_estudiante_completo(self, estudiante: Estudiante):
        """Guarda un estudiante y todas sus materias en la base de datos"""
        cursor = self.conexion.cursor()
        try:
            # Guardar estudiante
            cursor.execute('''
                INSERT OR REPLACE INTO estudiantes (cedula, nombre)
                VALUES (?, ?)
            ''', (estudiante.get_cedula(), estudiante.get_nombre()))

            # Guardar cada materia y su inscripción
            for materia in estudiante.materias:
                # Guardar materia
                cursor.execute('''
                    INSERT OR IGNORE INTO materias (codigo, nombre)
                    VALUES (?, ?)
                ''', (materia.get_codigo(), materia.get_nombre()))

                # Guardar inscripción
                cursor.execute('''
                    INSERT OR IGNORE INTO inscripciones (cedula_estudiante, codigo_materia)
                    VALUES (?, ?)
                ''', (estudiante.get_cedula(), materia.get_codigo()))

            self.conexion.commit()
            print(f"Estudiante {estudiante.get_nombre()} guardado con {len(estudiante.materias)} materias.")

        except sqlite3.Error as e:
            print(f"Error al guardar estudiante {estudiante.get_cedula()}: {e}")
            self.conexion.rollback()
            raise

    def obtener_estudiantes_por_materia(self, codigo_materia: str) -> list:
        """Obtiene todos los estudiantes inscritos en una materia específica"""
        cursor = self.conexion.cursor()
        try:
            cursor.execute('''
                SELECT e.cedula, e.nombre 
                FROM estudiantes e
                JOIN inscripciones i ON e.cedula = i.cedula_estudiante
                WHERE i.codigo_materia = ?
            ''', (codigo_materia,))
            
            return [Estudiante(cedula, nombre) for cedula, nombre in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error al consultar estudiantes por materia: {e}")
            return []

    def obtener_total_materias_estudiante(self, cedula: str) -> int:
        """Obtiene el total de materias inscritas por un estudiante"""
        cursor = self.conexion.cursor()
        try:
            cursor.execute('''
                SELECT COUNT(*) 
                FROM inscripciones 
                WHERE cedula_estudiante = ?
            ''', (cedula,))
            
            return cursor.fetchone()[0]
        except sqlite3.Error as e:
            print(f"Error al consultar total de materias: {e}")
            return 0
