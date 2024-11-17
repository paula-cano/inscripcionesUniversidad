import sqlite3
from src.programa.archivo import LectorArchivoTexto
from src.programa.validador import ValidadorDatos
from src.modelos.estudiante import Estudiante
from src.modelos.materia import Materia

class GestorBaseDatos:
    def __init__(self, url_db='inscripciones.db'):
        self.URL_DB = url_db
        self.conexion = None

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
                    FOREIGN KEY (codigo_materia) REFERENCES materias(codigo)
                )
            ''')
            
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al crear las tablas: {e}")
            raise
    
    #Obtiene un estudiante por su cédula     
    def obtener_estudiante(self, cedula: str):
        cursor = self.conexion.cursor()
        cursor.execute('''
            SELECT cedula, nombre
            FROM estudiantes
            WHERE cedula = ?
        ''', (cedula,))
        resultado = cursor.fetchone()
        return Estudiante(*resultado) if resultado else None
    
    #Guarda un estudiante si no existe
    def guardar_estudiante(self, cedula: str, nombre: str):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                INSERT OR IGNORE INTO estudiantes (cedula, nombre)
                VALUES (?, ?)
            ''', (cedula, nombre))
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al guardar el estudiante {cedula}: {e}")
            raise

        
        
    #Obtiene una materia por su código
    def obtener_materia(self, codigo: str):
        cursor = self.conexion.cursor()
        cursor.execute('''
            SELECT codigo, nombre
            FROM materias
            WHERE codigo = ?
        ''', (codigo,))
        resultado = cursor.fetchone()
        return Materia(*resultado) if resultado else None
        
        
    #Guarda una materia si no existe
    def guardar_materia(self, codigo: str, nombre: str):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                INSERT OR IGNORE INTO materias (codigo, nombre)
                VALUES (?, ?)
            ''', (codigo, nombre))
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al guardar la materia {codigo}: {e}")
            raise
        
        
    #Guarda una inscripción
    def guardar_inscripcion(self, cedula: str, codigo_materia: str):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                INSERT OR IGNORE INTO inscripciones (cedula_estudiante, codigo_materia)
                VALUES (?, ?)
            ''', (cedula, codigo_materia))
            self.conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al guardar la inscripción de {cedula} en la materia {codigo_materia}: {e}")
            raise

    #Obtiene todas las materias inscritas por un estudiante
    def obtener_materias_por_estudiante(self, cedula: str):
        try:
            cursor = self.conexion.cursor()
            cursor.execute('''
                SELECT m.codigo, m.nombre
                FROM materias m
                JOIN inscripciones i ON m.codigo = i.codigo_materia
                WHERE i.cedula_estudiante = ?
            ''', (cedula,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al obtener las materias del estudiante {cedula}: {e}")
            return []
    
    #Obtiene todos los estudiantes inscritos en una materia específica
    def obtener_estudiantes_por_materia(self, codigo: str) -> list:
        cursor = self.conexion.cursor()
        try:
            cursor.execute('''
                SELECT e.cedula, e.nombre 
                FROM estudiantes e
                JOIN inscripciones i ON e.cedula = i.cedula_estudiante
                WHERE i.codigo_materia = ?
            ''', (codigo,))
            
            estudiantes = cursor.fetchall()
            return[{"cedula": cedula, "nombre": nombre} for cedula, nombre in estudiantes]
        except sqlite3.Error as e:
            print(f"Error al obtener los estudiantes de la materia {codigo}: {e}")
            return []

    #Obtiene el total de materias inscritas por un estudiante
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
