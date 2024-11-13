class Estudiante:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
            self._cedula = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
            self._nombre = value

    def __repr__(self):
        return f"Estudiante(cedula={self.cedula}, nombre='{self.nombre}')"