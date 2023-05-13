from tabulate import tabulate
from .services.dataServices import ExcelFileService


PATH_EXCEL="./src/excels/establecimientos.xlsx"
excel_service = ExcelFileService(PATH_EXCEL)

class Establecimiento:
    def __init__(self):
        try: 
            self.__codigo=input("Ingrese el codigo: ")
            self.__ruc=input("Ingrese el ruc: ")
            self.__nombre=input("Ingrese la razon social: ")
            
            
        except ValueError as error:
            print(f"Ingrese solo numeros validos: {error}")
        except Exception as error:
            print("Error al ingresar los valores")
        else:
            print("Sin errores")
        
    
    def registrar(self):
        records = excel_service.read_file()
        record = [self.__build_record()]
        excel_service.update_file(records + record)
        print("El establecimiento a sido registrado")
    
    def actualizar(self, num):
        record = self.__build_record()
        records = excel_service.read_file()
        records[num-1] = record
        excel_service.update_file(records)
        print(f"Se ha actualizado el registro {num}\n")
    
    def __build_record(self):
        return {
            "codigo": self.__codigo,
            "ruc": self.__ruc,
            "nombre": self.__nombre
        }
    
    @classmethod
    def eliminar(cls, num):
        records = excel_service.read_file()
        deleted_record = records.pop(num-1)
        
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
