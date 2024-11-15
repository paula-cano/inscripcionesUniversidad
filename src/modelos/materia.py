class Materia:
    
    def __init__(self, codigo: str, nombre: str):
        self.codigo = codigo
        self.nombre = nombre

    def __eq__(self, other):
        if isinstance(other, Materia):
            return self.codigo == other.codigo
        return False

    def __hash__(self):
        # Define un hash basado en el código para evitar duplicados en conjuntos (Set)
        return hash(self.codigo)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    #setters
    def set_codigo(self, codigo: str):
        self.codigo = codigo
        
    def set_nombre(self, nombre: str):
        self.nombre = nombre
        
    #getters
    def get_codigo(self):
        return self.codigo
    
    def get_nombre(self):
        return self.nombre
    