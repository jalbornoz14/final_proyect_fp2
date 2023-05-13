from etc.env import Env
from tabulate import tabulate

from src.empleados import Empleado
from src.establecimientos import Establecimiento
from src.pacientes import Paciente
# from src.registros import Registro
from src.vacunas import Vacuna

MODELS = {
    1: Empleado,
    2: Establecimiento,
    3: Paciente,
    4: Vacuna
}


class Menu:

    def __init__(self):
        self.opcion = -1

    @property
    def opciones(self):
        return [["(1)", "Empleados"], ["(2)", "Establecimiento"], ["(3)", "Pacientes"], ["(4)", "Vacunas"], ["(5)", "Registros"], ["(0)", "<-- Salir"]]

    def mostrar_menu(self):
        encabezados = ["Opción", "Menu Principal"]
        estilo = Env.TABULATE_STYLE
        print(tabulate(self.opciones, headers=encabezados, tablefmt=estilo))

    def mostrar_sub_menu(self,menu, sub_menu):
        sub_menu = sub_menu
        encabezados = ["Opción", "Sub Menu de " + str(self.opciones[menu-1][1])]
        estilo = Env.TABULATE_STYLE
        
        print(tabulate(sub_menu, headers=encabezados, tablefmt=estilo))

    def sub_menu(self, menu, opcion, model):

        if 1 <= menu <= 4:
            return self.__menu_crud(opcion, model)
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
                self.sub_menu(5, int(input("Seleccione una opción de menu: ")), None)
            elif opcion == 0:
                print("Ha seleccionado la opción Salir.")
                return False
            return True
        except ValueError as e:
            print("Opción inválida. Seleccione una opción válida.")
            return True
    
    def iniciar(self):
        while self.ejecutar_opcion():
            self.mostrar_menu()
            self.seleccionar_opcion()
    
    def __show_sub_menu(self, opcion):
        model =  MODELS[opcion]
        sub_menu = [["(1)", "Nuevo"], ["(2)", "Editar"], ["(3)", "Listar"], ["(4)", "Eliminar"], ["(0)", "<-- Volver"]]
        return_to_main_menu = False
        while not return_to_main_menu:
            self.mostrar_sub_menu(opcion, sub_menu)
            try:
                return_to_main_menu = self.sub_menu(opcion, int(input("Seleccione una opción de menu: ")), model)
            except Exception as e:
                print("Escoga una de las opciones del menu\n")
    
    @staticmethod            
    def __menu_crud(opcion, model):
        if opcion == 1:
            print("Completemos los campos a continuacion:\n")
            instance = model()
            instance.registrar()  
        elif opcion == 2:
            record_num = int(input("Escriba el numero de registro a actualizar: "))
            instance = model()
            instance.actualizar(record_num)
        elif opcion == 3:
            model.listar()
        elif opcion == 4:
            record_num = int(input("Escriba el numero de registro a eliminar: "))
            model.eliminar(record_num)
        elif opcion == 0:
            print("Ha seleccionado la opción Volver.\n\n")
            return True
        else:
            print("Opción inválida. Seleccione una opción válida.\n")
        return False
            
    