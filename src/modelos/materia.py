class Materia:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    def __repr__(self):
        return f"Materia(codigo={self.codigo}, nombre='{self.nombre}')"