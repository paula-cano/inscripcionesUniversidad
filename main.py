# main.py
from src.ui.interface import InterfazConsola

def main():
    try:
        interfaz = InterfazConsola()
        interfaz.mostrarMenu()
    except Exception as e:
        print(f"Error en la aplicación: {e}")

if __name__ == "__main__":
    main()