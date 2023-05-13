from tabulate import tabulate
from .services.dataServices import ExcelFileService


PATH_EXCEL="./src/excels/pacientes.xlsx"
excel_service = ExcelFileService(PATH_EXCEL)

class Paciente:
    
    def __init__(self):
        try: 
            self.__codigo=input("Ingrese el codigo: ")
            self.__dni=input("Ingrese DNI: ")
            self.__apellidos=str(input("Ingrese Apellidos: "))
            self.__nombres=input("Ingrese Nombres: ")
            self.__telefono=input("Ingrese telefono: ")
            self.__direccion=input("Ingrese direccion: ")
            self.__email=input("Ingrese email: ")
            
        except ValueError as error:
            print(f"Ingrese solo numeros validos: {error}")
        except Exception as error:
            print("Error al ingresar los valores")
        else:
            print("Sin errores\n")
        
    def registrar(self):
        records = excel_service.read_file()
        record = [self.__build_record()]
        excel_service.update_file(records + record)
        print("La vacuna ha sido registrada\n")
    
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
            "dni": self.__dni,
            "apellidos": self.__apellidos,
            "nombres": self.__nombres,
            "telefono": self.__telefono,
            "direccion": self.__direccion,
            "email": self.__email,
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
