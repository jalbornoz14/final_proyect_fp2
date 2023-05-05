class Establecimiento:
    def __init__(self):
        try: 
            self.__codigo=int(input("Ingrese codigo: "))
            self.__ruc=input("Ingrese DNI: ")
            self.__nombre=input("Ingrese Apellidos: ")
            
            
        except ValueError as error:
            print(f"Ingrese solo numeros validos: {error}")
        except Exception as error:
            print("Error al ingresar los valores")
        else:
            print("Sin errores")
        
    
    @property
    def codigo(self):
        return self.__codigo
        
    @property
    def ruc(self):
        return self.__ruc
        
    @property
    def nombre(self):
        return self.__nombre
        
     
    @codigo.setter
    def codigo(self,value):
        self.__codigo=value  
        
    @ruc.setter
    def ruc(self,value):
        self.__ruc=value 
   
    @nombre.setter
    def nombre(self,value):
        self.__nombre=value  
        
    
        
    def Imprimir(self):
        try:
            print(f"Datos de establecimiento")
            print(f"Codigo: {self.codigo}")
            print(f"RUC: {self.ruc}")
            print(f"Nombre:  {self.nombre}")
            
        except:
            print("Error en ingreso de datos")
            
e1=Establecimiento()
e1.Imprimir()
