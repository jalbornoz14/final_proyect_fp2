class Vacunados:
    def __init__(self):
        try: 
            self.__codigo=int(input("Ingrese codigo: "))
            self.__dni=int(input("Ingrese DNI: "))
            self.__apellidos=str(input("Ingrese Apellidos: "))
            self.__nombres=input("Ingrese Nombres: ")
            self.__telefono=int(input("Ingrese telefono: "))
            self.__direccion=input("Ingrese direccion: ")
            self.__email=input("Ingrese email: ")
            
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
    def dni(self):
        return self.__dni
        
    @property
    def apellidos(self):
        return self.__apellidos
        
    @property
    def nombres(self):
        return self.__nombres
    
    @property
    def telefono(self):
        return self.__telefono
        
    @property
    def direccion(self):
        return self.__direccion
        
    @property
    def email(self):
        return self.__direccion
                
    @codigo.setter
    def codigo(self,value):
        self.__codigo=value  
        
    @dni.setter
    def dni(self,value):
        self.__dni=value 
   
    @apellidos.setter
    def apellidos(self,value):
        self.__apellidos=value  
        
    @nombres.setter
    def nombres(self,value):
        self.__nombres=value 
        
    @telefono.setter
    def telefono(self,value):
        self.__telefono=value  
        
    @direccion.setter
    def direccion(self,value):
        self.__direccion=value 
    
    @email.setter
    def email(self,value):
        self.__email=value  
        
    def Imprimir(self):
        try:
            print(f"Datos de persona vacunada")
            print(f"Codigo: {self.codigo}")
            print(f"DNI: {self.dni}")
            print(f"Apellidos:  {self.apellidos}")
            print(f"Nombres:  {self.nombres}")
            print(f"Telefono:  {self.telefono}")
            print(f"Direccion:  {self.direccion}")
            print(f"Email:  {self.email}")
        except:
            print("Error en ingreso de datos")
            
            

        
    
v1=Vacunados()
v1.Imprimir()