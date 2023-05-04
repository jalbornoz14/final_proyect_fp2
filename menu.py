from etc.env import Env
from tabulate import tabulate


class Menu:

    def __init__(self):
        self.opcion = -1

    @property
    def opciones(self):
        return [["(1)", "Vacunados"], ["(2)", "Empleado"], ["(3)", "Establecimiento"], ["(4)", "Vacuna"], ["(5)", "Registro"], ["(0)", "<-- Salir"]]

    def mostrar_menu(self):
        encabezados = ["Opción", "Menu Principal"]
        estilo = Env.TABULATE_STYLE
        print(tabulate(self.opciones, headers=encabezados, tablefmt=estilo))

    def mostrar_sub_menu(self,menu, sub_menu):
        sub_menu = sub_menu
        encabezados = ["Opción", "Sub Menu de " +
                       str(self.opciones[menu-1][1])]
        estilo = Env.TABULATE_STYLE
        print(tabulate(sub_menu, headers=encabezados, tablefmt=estilo))

    def sub_menu(self, menu, opcion):
        if menu == 1:
            if opcion == 1:
                print("Ahora vamos a registrar un nuevo vacunado.")
            elif opcion == 2:
                print("Ahora vamos a editar un vacunado.")
            elif opcion == 3:
                print("Ahora vamos a listar los vacunados.")
            elif opcion == 4:
                print("Ahora vamos a eliminar un vacunado.")
            elif opcion == 0:
                print("Ha seleccionado la opción Volver.")
                return False
            else:
                print("Opción inválida. Seleccione una opción válida.")
        elif menu == 2:
            if opcion == 1:
                print("Ahora vamos a registrar un nuevo empleado.")
            elif opcion == 2:
                print("Ahora vamos a editar un empleado.")
            elif opcion == 3:
                print("Ahora vamos a listar los empleados.")
            elif opcion == 4:
                print("Ahora vamos a eliminar un empleado.")
            elif opcion == 0:
                print("Ha seleccionado la opción Volver.")
                return False
            else:
                print("Opción inválida. Seleccione una opción válida.")
        elif menu == 3:
            if opcion == 1:
                print("Ahora vamos a registrar un nuevo establecimiento.")
            elif opcion == 2:
                print("Ahora vamos a editar un establecimiento.")
            elif opcion == 3:
                print("Ahora vamos a listar los establecimientos.")
            elif opcion == 4:
                print("Ahora vamos a eliminar un establecimiento.")
            elif opcion == 0:
                print("Ha seleccionado la opción Volver.")
                return False
            else:
                print("Opción inválida. Seleccione una opción válida.")
        elif menu == 4:
            if opcion == 1:
                print("Ahora vamos a registrar una nueva vacuna.")
            elif opcion == 2:
                print("Ahora vamos a editar una vacuna.")
            elif opcion == 3:
                print("Ahora vamos a listar las vacunas.")
            elif opcion == 4:
                print("Ahora vamos a eliminar una vacuna.")
            elif opcion == 0:
                print("Ha seleccionado la opción Volver.")
                return False
            else:
                print("Opción inválida. Seleccione una opción válida.")
        elif menu == 5:
            if opcion == 1:
                print("Ahora vamos a registrar un nuevo registro.")
            elif opcion == 2:
                print("Ahora vamos a listar los registros.")
            elif opcion == 0:
                print("Ha seleccionado la opción Volver.")
                return False
            else:
                print("Opción inválida. Seleccione una opción válida.")
        else:
            print("Opción inválida. Seleccione una opción válida.")

    def seleccionar_opcion(self):
        self.opcion = input("Seleccione una opción: ")

    def ejecutar_opcion(self):

        try:
            opcion = int(self.opcion)
            if opcion == 1:
                sub_menu = [["(1)", "Nuevo"], ["(2)", "Editar"], ["(3)", "Listar"], ["(4)", "Eliminar"], ["(0)", "<-- Volver"]]
                self.mostrar_sub_menu(1, sub_menu)
                self.sub_menu(1, int(input("Seleccione una opción de menu: ")))
            elif opcion == 2:
                sub_menu = [["(1)", "Nuevo"], ["(2)", "Editar"], ["(3)", "Listar"], ["(4)", "Eliminar"], ["(0)", "<-- Volver"]]
                self.mostrar_sub_menu(2, sub_menu)
                self.sub_menu(2, int(input("Seleccione una opción de menu: ")))
            elif opcion == 3:
                sub_menu = [["(1)", "Nuevo"], ["(2)", "Editar"], ["(3)", "Listar"], ["(4)", "Eliminar"], ["(0)", "<-- Volver"]]
                self.mostrar_sub_menu(3, sub_menu)
                self.sub_menu(3, int(input("Seleccione una opción de menu: ")))
            elif opcion == 4:
                sub_menu = [["(1)", "Nuevo"], ["(2)", "Editar"], ["(3)", "Listar"], ["(4)", "Eliminar"], ["(0)", "<-- Volver"]]
                self.mostrar_sub_menu(4, sub_menu)
                self.sub_menu(4, int(input("Seleccione una opción de menu: ")))
            elif opcion == 5:
                sub_menu = [["(1)", "Nuevo"], ["(2)", "Listar"], ["(0)", "<-- Volver"]]
                self.mostrar_sub_menu(5, sub_menu)
                self.sub_menu(5, int(input("Seleccione una opción de menu: ")))
            elif opcion == 0:
                print("Ha seleccionado la opción Salir.")
                return False
            return True
        except ValueError:
            print("Opción inválida. Seleccione una opción válida.")
            return True

    def iniciar(self):
        while self.ejecutar_opcion():
            self.mostrar_menu()
            self.seleccionar_opcion()
