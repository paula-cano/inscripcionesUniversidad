class LectorArchivoTexto:
    def __init__(self):
        pass

    def obtener_lineas(self, ruta: str):
        # Abre el archivo, lee y devuelve las líneas
        with open(ruta, "r") as file:
            lineas = file.readlines()
        return lineas
