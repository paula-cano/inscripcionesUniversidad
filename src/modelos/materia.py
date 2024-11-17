class Materia:
    
    def __init__(self, codigo: str, nombre: str):
        self.codigo = codigo
        self.nombre = nombre
        
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if not value.isdigit():
            raise ValueError("El código debe ser numérico.")
        self._codigo = value.strip()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value.strip()


    def __eq__(self, other):
        if isinstance(other, Materia):
            return self.codigo == other.codigo
        return False

    def __hash__(self):
        # Define un hash basado en el código para evitar duplicados en conjuntos (Set)
        return hash(self.codigo)

    def __str__(self):
        return f"Materia(código: {self.codigo}, nombre: {self.nombre})"

    
