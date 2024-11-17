class Estudiante:
    def __init__(self, cedula: str, nombre: str):
        self.cedula = cedula
        self.nombre = nombre
        
    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        if not value.isdigit() or len(value.strip()) <= 5:
            raise ValueError("La cédula debe ser numérica y tener más de 5 dígitos.")
        self._cedula = value.strip()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if len(value.strip()) <= 2:
            raise ValueError("El nombre debe tener más de 2 caracteres.")
        self._nombre = value.strip()

    def __str__(self):
        return f"Estudiante(cédula: {self.cedula}, nombre: {self.nombre})"

    def __eq__(self, other):
        if isinstance(other, Estudiante):
            return self.cedula == other.cedula
        return False

    def __hash__(self):
        return hash(self.cedula)
    