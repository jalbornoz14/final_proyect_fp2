from tabulate import tabulate
from .services.dataServices import ExcelFileService


PATH_EXCEL="./src/excels/empleados.xlsx"
excel_service = ExcelFileService(PATH_EXCEL)

class Empleado:
    def __init__(self):
        self.__codigo = input("Ingresa el codigo:")
        self.__dni = input("Ingresa el dni:")
        self.__tipo = input("Ingresa la tipo:")
        self.__turno = input("Ingresa el turno:")
        self.__apellidos = input("Ingresa la fecha de vencimiento:")
        self.__email = input("Ingresa el email:")
        self.__password = input("Ingresa el password:")
        self.__direccion = input("Ingresa la direccion:")
    
    def registrar(self):
        records = excel_service.read_file()
        record = [self.__build_record()]
        excel_service.update_file(records + record)
        print("El empleado ha sido registrado")
    
    def actualizar(self, num):
        record = self.__build_record()
        records = excel_service.read_file()
        if not records:
            print("No tiene registros por actualiza\nr")
        elif num > len(records) or num < 0:
            print("No es un registro valido\n")
        else:
            records[num] = record
            excel_service.update_file(records)
            print(f"Se ha actualizado el registro {num}\n")
    
    def __build_record(self):
        return {
            "codigo": self.__codigo,
            "dni": self.__dni,
            "tipo": self.__tipo,
            "turno": self.__turno,
            "apellidos": self.__apellidos,
            "email": self.__email,
            "password": self.__password,
            "direccion": self.__direccion,
        }
    
    @classmethod
    def eliminar(cls, num):
        records = excel_service.read_file()
        
        if not records:
            print("No tiene registros para eliminar\n")
        elif num > len(records) or num < 0:
            print("No es un registro valido\n")
        else:
            deleted_record = records.pop(num)
        
            print("Se ha eliminado el siguiente registro\n")
            excel_service.format_data([deleted_record])
            
            excel_service.update_file(records)
        
    @classmethod
    def listar(cls):
        data = excel_service.read_file()
        if not data:
            print("Agrega un nuevo registro para mostrar la tabla\n")
        else:
            excel_service.format_data(data)
