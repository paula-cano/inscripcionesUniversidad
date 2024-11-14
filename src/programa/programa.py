from src.ui.interface import InterfazConsola


class ProgramaReporteInscripciones:
    def __init__(self):
        self.interfaz = InterfazConsola()

    def iniciar(self):
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        # Muestra el menú de la interfaz de consola
        self.interfaz.mostrar_menu()