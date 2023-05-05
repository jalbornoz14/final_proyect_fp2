import openpyxl as xl

class Vacuna:
    
    def __init__(self, codigo, laboratorio, efectividad, lote, vencimiento):
        self.__codigo = codigo
        self.__laboratorio = laboratorio
        self.__efectividad = efectividad
        self.__lote = lote
        self.__vencimiento = vencimiento
        
    def registrar(self):
        pass
    
    def actualizar(self, codigo):
        pass
    
    def eliminar(self, codigo):
        pass
    
    def lista(self):
        pass
    
    
    def __get_information(self):
        data_service = ExcelFileService('vacunas.xlsx')
        return data_service.read_file()
        
    
    
    
    