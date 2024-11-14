# src/validador_datos.py

class ValidadorDatos:
    def validar_cedula(self, cedula: str):
        return cedula.isdigit() and len(cedula) > 5

    def validar_nombre(self, nombre: str):
        return nombre.isalpha() and len(nombre) > 2

    def validar_codigo_materia(self, codigo: str):
        return codigo.isdigit()

    def validar_formato_linea(self, linea: str):
        partes = linea.strip().split(",")
        return (
            len(partes) == 4 and
            self.validar_cedula(partes[0]) and
            self.validar_nombre(partes[1]) and
            self.validar_codigo_materia(partes[2])
        )

    def detectar_duplicados(self, datos: list):
        # Detecta duplicados en la lista de datos
        return list(set([dato for dato in datos if datos.count(dato) > 1]))
