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
    
    def __leer_excel(self):
        try:
            wb = xl.load_workbook('vacunas.xlsx')
            sheet = wb.active['Hoja1']
            sheet['E1'] = 'Total'
            for row in range(2, sheet.max_row + 1):
                qty = sheet.cell(row, 3).value
                price = sheet.cell(row, 4).value
                total = qty * price
                sheet.cell(row, 5).value = total
 
            #save in this proyect
            wb.save('vacunas.xlsx')
        except Exception as e:
            print(e)
    
    def __guardar_excel(self):
        pass
        
    
    
    
    