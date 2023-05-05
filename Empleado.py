class Empleado:
    def __init__(self):
        try: 
            self.__codigoe=int(input("Ingrese codigo: "))
            self.__dnie=input("Ingrese DNI: ")
            self.__tipoe=int(input("Ingrese tipo de empleado: si es enfermera=01, si es tecnico de enfermeria=02 y si es doctor=03: "))
            self.__turnoe=int(input("Ingrese turno de empleado: si es turno de 7am a 7pm =01y si es turno de 7pm a 7am=02: "))
            self.__apellidose=input("Ingrese Apellidos: ")
            self.__nombrese=input("Ingrese Nombres: ")
            self.__login=input("Ingrese login o usuario: ")
            self.__password=input("Ingrese contraseña: ")
            
        except ValueError as error:
            print(f"Ingrese solo datos validos: {error}")
        except Exception as error:
            print("Error al ingresar los valores")
        else:
            print("Sin errores")
    
    @property
    def codigoe(self):
        return self.__codigoe
        
    @property
    def dnie(self):
        return self.__dnie
        
     
    @property
    def tipoe(self):
        return self.__tipoe
        
    @property
    def turnoe(self):
        return self.__turnoe
        
    @property
    def apellidose(self):
        return self.__apellidose
        
    @property
    def nombrese(self):
        return self.__nombrese
    
    @property
    def login(self):
        return self.__login
        
    @property
    def password(self):
        return self.__password
        
    @property
    def email(self):
        return self.__direccion
                
    @codigoe.setter
    def codigoe(self,value):
        self.__codigoe=value  
        
    @dnie.setter
    def dnie(self,value):
        self.__dnie=value 
    
    @tipoe.setter
    def tipoe(self,value):
        self.__tipoe=value  
        
    @turnoe.setter
    def turnoe(self,value):
        self.__turnoe=value 
   
    @apellidose.setter
    def apellidose(self,value):
        self.__apellidose=value  
        
    @nombrese.setter
    def nombrese(self,value):
        self.__nombrese=value 
        
    @login.setter
    def login(self,value):
        self.__login=value  
        
    @password.setter
    def password(self,value):
        self.__password=value 
    
    
        
    def Imprimir(self):
        try:
            print(f"Datos de empleado")
            print(f"Codigo: {self.codigoe}")
            print(f"DNI: {self.dnie}")
            print(f"Tipo de empleado: {self.tipoe}")
            print(f"Turno: {self.turnoe}")
            print(f"Apellidos:  {self.apellidose}")
            print(f"Nombres:  {self.nombrese}")
            print(f"Login:  {self.login}")
            print(f"Password:  {self.password}")
            
        except:
            print("Error en ingreso de datos")
e1=Empleado()
e1.Imprimir()