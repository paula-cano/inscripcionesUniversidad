class InterfazConsola:
    def __init__(self):
        # Puedes inicializar más componentes si es necesario
        pass

    def mostrarMenu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Cargar archivo de inscripciones")
            print("2. Mostrar total de materias por estudiante")
            print("3. Filtrar estudiantes por materia")
            print("4. Exportar datos a JSON/CSV")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.cargarArchivo()
            elif opcion == "2":
                self.mostrarEstudiantes()
            elif opcion == "3":
                self.filtrarPorMateria()
            elif opcion == "4":
                self.exportarDatos()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    # Define otros métodos como cargarArchivo(), mostrarEstudiantes(), etc.
