from tabulate import tabulate
from .services.dataServices import ExcelFileService


PATH_EXCEL="./src/excels/vacunas.xlsx"
excel_service = ExcelFileService(PATH_EXCEL)

class Vacuna:
        
    def __init__(self, codigo, laboratorio, efectividad, lote, vencimiento):
        self.__codigo = codigo
        self.__laboratorio = laboratorio
        self.__efectividad = efectividad
        self.__lote = lote
        self.__vencimiento = vencimiento
        
    def registrar(self):
        records = excel_service.read_file()
        record = [{
            "codigo": self.__codigo,
            "laboratorio": self.__laboratorio,
            "efectividad": self.__efectividad,
            "vencimiento": self.__vencimiento,
            "lote": self.__lote
        }]
        excel_service.update_file(records + record)
        print("La vacuna a sido registrada")
    
    def actualizar(self, num):
        record = {
            "codigo": self.__codigo,
            "laboratorio": self.__laboratorio,
            "efectividad": self.__efectividad,
            "vencimiento": self.__vencimiento,
            "lote": self.__lote
        }
        records = excel_service.read_file()
        records[num-1] = record
        excel_service.update_file(records)
        print(f"Se ha actualizado el registro {num}\n")
    
    @classmethod
    def eliminar(cls, num):
        records = excel_service.read_file()
        deleted_record = records.pop(num-1)
        
        print("Se ha eliminado el siguiente registro\n")
        print(deleted_record)
        
        excel_service.update_file(records)
    
    @classmethod
    def lista(cls):
        print(excel_service.read_file())
        
    @classmethod
    def ask_variables(cls):
        return [
            input("Ingresa el codigo:"),
            input("Ingresa el laboratorio:"),
            input("Ingresa la efectividad:"),
            input("Ingresa el lote:"),
            input("Ingresa la fecha de vencimiento:"),
        ]
    
#    @staticmethod
#   def format_register():
        
    
    
    
    