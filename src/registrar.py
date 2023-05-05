class RegistroVacunacion:
    def __init__(self):
        try:
            self.codigo_establecimiento=int(input("Ingrese codigo de Establecimiento: "))
            self.codigo_empleado=int(input("Ingrese codigo de Empleado: "))
            self.codigo_vacunado=int(input("Ingrese codigo de Vacunado: "))
            self.codigo_vacuna=int(input("Ingrese codigo de Vacuna: "))
            self.nombre_establecimiento=str(input("Ingrese Nombre del Establecimiento: "))
            self.nombre_empleado=str(input("Ingrese Nombre del Empleado: "))
            self.nombre_vacunado=str(input("Ingrese Nombre del Vacunado: "))
            
        except ValueError as error:
            print(f"Ingrese solo datos validos: {error}")
        except Exception as error:
            print("Error al ingresar los valores")
        else:
            print("Sin errores")
            
    @property
    def codigo_establecimiento(self):
        return self.__codigo_establecimiento
        
    @property
    def codigo_empleado(self):
        return self.__codigo_empleado
        
    @property
    def codigo_vacunado(self):
        return self.__codigo_vacunado
        
    @property
    def codigo_vacuna(self):
         return self.__codigo_vacuna
        
    @property
    def nombre_establecimiento(self):
         return self.__nombre_establecimiento
        
    @property
    def nombre_empleado(self):
         return self.__nombre_empleado
    
    @property
    def nombre_vacunado(self):
         return self.__nombre_vacunado
        
    @codigo_establecimiento.setter
    def codigo_establecimiento(self,value):
        self.__codigo_establecimiento=value  
        
    @codigo_empleado.setter
    def codigo_empleado(self,value):
        self.__codigo_empleado=value 
    
    @codigo_vacunado.setter
    def codigo_vacunado(self,value):
        self.__codigo_vacunado=value  
        
    @codigo_vacuna.setter
    def codigo_vacuna(self,value):
        self.__codigo_vacuna=value 
   
    @nombre_establecimiento.setter
    def nombre_establecimiento(self,value):
        self.__nombre_establecimiento=value  
        
    @nombre_empleado.setter
    def nombre_empleado(self,value):
        self.__nombre_empleado=value 
        
    @nombre_vacunado.setter
    def nombre_vacunado(self,value):
        self.__nombre_vacunado=value 

    def Imprimir(self):
        try:
            print(f"Registro de Vacunacion")
            print(f"Codigo: {self.codigo_establecimiento}")
            print(f"DNI: {self.codigo_empleado}")
            print(f"Tipo de empleado: {self.codigo_vacunado}")
            print(f"Turno: {self.codigo_vacuna}")
            print(f"Apellidos:  {self.nombre_establecimiento}")
            print(f"Nombres:  {self.nombre_empleado}")
            print(f"Login:  {self.nombre_vacunado}")
            
        except:
            print("Error en ingreso de datos")


r1=RegistroVacunacion()
r1.Imprimir() 
                    
        
