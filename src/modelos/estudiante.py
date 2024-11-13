from src.modelos.materia import Materia
import json

class Estudiante:
    def __init__(self, cedula: str, nombre: str):
        self.cedula = cedula
        self.nombre = nombre
        self.materias = set()  # Utilizamos un conjunto para evitar materias duplicadas

    def adicionar_materia(self, codigo: str, nombre: str) -> bool:
        materia = Materia(codigo, nombre)
        # Intenta añadir la materia al conjunto; True si es nueva, False si ya existía
        if materia not in self.materias:
            self.materias.add(materia)
            return True
        return False

    def get_total_materias(self) -> int:
        return len(self.materias)

    def to_string(self) -> str:
        materias_str = ", ".join(str(materia) for materia in self.materias)
        return f"Estudiante: {self.cedula} - {self.nombre} | Materias: {materias_str}"

    def to_json(self) -> str:
        estudiante_dict = {
            "cedula": self.cedula,
            "nombre": self.nombre,
            "materias": [{"codigo": materia.codigo, "nombre": materia.nombre} for materia in self.materias]
        }
        return json.dumps(estudiante_dict, indent=4)

    def to_csv(self) -> str:
        materias_csv = "\n".join(f"{self.cedula},{self.nombre},{materia.codigo},{materia.nombre}" for materia in self.materias)
        return materias_csv

    def __eq__(self, other):
        if isinstance(other, Estudiante):
            return self.cedula == other.cedula
        return False

    def __hash__(self):
        # Define un hash basado en la cédula del estudiante para evitar duplicados
        return hash(self.cedula)