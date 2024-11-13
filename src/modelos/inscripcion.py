class Inscripcion:
    def __init__(self, estudiante, materia):
        self.estudiante = estudiante
        self.materia = materia

    @property
    def estudiante_cedula(self):
        return self._estudiante_cedula

    @estudiante_cedula.setter
    def estudiante_cedula(self, value):
        self._estudiante_cedula = value

    @property
    def materia_codigo(self):
        return self._materia_codigo

    @materia_codigo.setter
    def materia_codigo(self, value):
        self._materia_codigo = value
