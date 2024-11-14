from src.programa.validador import ValidadorDatos

class LectorArchivoTexto:
    def __init__(self):
        self.nombre_archivo = ""
        self.validador = ValidadorDatos()

    def obtener_lineas(self, ruta: str):
        # Abre el archivo, lee y devuelve las líneas
        with open(ruta, "r") as file:
            lineas = file.readlines()
        return lineas

    def cerrar_recursos(self):
        # Método reservado para cerrar recursos adicionales si es necesario
        pass
