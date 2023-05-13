from etc.env import Env
from tabulate import tabulate

from src.vacuna import Vacuna


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
                return True
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
                return True
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
                return True
            else:
                print("Opción inválida. Seleccione una opción válida.")
        elif menu == 4:
            return self.__menu_vacunas(opcion)
        elif menu == 5:
            if opcion == 1:
                print("Ahora vamos a registrar un nuevo registro.")
            elif opcion == 2:
                print("Ahora vamos a listar los registros.")
            elif opcion == 0:
                print("Ha seleccionado la opción Volver.")
                return True
            else:
                print("Opción inválida. Seleccione una opción válida.")
        else:
            print("Opción inválida. Seleccione una opción válida.")

    def seleccionar_opcion(self):
        self.opcion = input("Seleccione una opción: ")

    def ejecutar_opcion(self):
        
        try:
            opcion = int(self.opcion)
            if 1<= opcion <= 4:
                self.__show_sub_menu(opcion)
                
            elif opcion == 5:
                sub_menu = [["(1)", "Nuevo"], ["(2)", "Listar"], ["(0)", "<-- Volver"]]
                self.mostrar_sub_menu(5, sub_menu)
                self.sub_menu(5, int(input("Seleccione una opción de menu: ")))
            elif opcion == 0:
                print("Ha seleccionado la opción Salir.")
                return False
            return True
        except ValueError as e:
            print(e)
            print("Opción inválida. Seleccione una opción válida.")
            return True
    
    def iniciar(self):
        while self.ejecutar_opcion():
            self.mostrar_menu()
            self.seleccionar_opcion()
    
    def __show_sub_menu(self, opcion):
        sub_menu = [["(1)", "Nuevo"], ["(2)", "Editar"], ["(3)", "Listar"], ["(4)", "Eliminar"], ["(0)", "<-- Volver"]]
        return_to_main_menu = False
        while not return_to_main_menu:
            self.mostrar_sub_menu(opcion, sub_menu)
            return_to_main_menu = self.sub_menu(opcion, int(input("Seleccione una opción de menu: ")))
    
    @staticmethod            
    def __menu_vacunas(opcion):
        if opcion == 1:
            vacuna_vars = Vacuna.ask_variables()
            vacuna = Vacuna(*vacuna_vars)
            vacuna.registrar()  
        elif opcion == 2:
            record_num = int(input("Escriba el numero de registro a eliminar"))
            vacuna_vars = Vacuna.ask_variables()
            vacuna = Vacuna(*vacuna_vars)
            vacuna.actualizar(record_num)
        elif opcion == 3:
            Vacuna.lista()
        elif opcion == 4:
            record_num = int(input("Escriba el numero de registro a eliminar"))
            Vacuna.eliminar(record_num)
        elif opcion == 0:
            print("Ha seleccionado la opción Volver.")
            return True
        else:
            print("Opción inválida. Seleccione una opción válida.")
        return False
            
    