from tabulate import tabulate
from .services.dataServices import ExcelFileService


PATH_EXCEL="./src/excels/vacunas.xlsx"
excel_service = ExcelFileService(PATH_EXCEL)

class Vacuna:
        
    def __init__(self):
        self.__codigo = input("Ingresa el codigo:")
        self.__laboratorio = input("Ingresa el laboratorio:")
        self.__efectividad = input("Ingresa la efectividad:")
        self.__lote = input("Ingresa el lote:")
        self.__vencimiento = input("Ingresa la fecha de vencimiento:")
        
    def registrar(self):
        records = excel_service.read_file()
        record = [self.__build_record()]
        excel_service.update_file(records + record)
        print("La vacuna ha sido registrada")
    
    def actualizar(self, num):
        record = self.__build_record()
        records = excel_service.read_file()
        if not records:
            print("No tiene registros por actualizar\n")
        elif num > len(records) or num < 0:
            print("No es un registro valido\n")
        else:
            records[num] = record
            excel_service.update_file(records)
            print(f"Se ha actualizado el registro {num}\n")
    
    def __build_record(self):
        return {
            "codigo": self.__codigo,
            "laboratorio": self.__laboratorio,
            "efectividad": self.__efectividad,
            "vencimiento": self.__vencimiento,
            "lote": self.__lote
        }
    
    @classmethod
    def eliminar(cls, num):
        records = excel_service.read_file()

        if not records:
            print("No tiene registros para eliminar\n")
        elif num >= len(records) or num < 0:
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
