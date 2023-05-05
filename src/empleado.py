empleados = []

class Empleado:
    def __init__(self):
        pass
    
    @property
    def codigo(self):
        return self.__codigo
        
    @property
    def dni(self):
        return self.__dni
     
    @property
    def tipo(self):
        return self.__tipo
        
    @property
    def turno(self):
        return self.__turno
        
    @property
    def apellidos(self):
        return self.__apellidos
        
    @property
    def nombres(self):
        return self.__nombres
    
    @property
    def login(self):
        return self.__login
        
    @property
    def password(self):
        return self.__password
        
    @property
    def email(self):
        return self.__direccion
                
    @codigo.setter
    def codigo(self,value):
        self.__codigo=value  
        
    @dni.setter
    def dni(self,value):
        self.__dni=value 
    
    @tipo.setter
    def tipo(self,value):
        self.__tipo=value  
        
    @turno.setter
    def turno(self,value):
        self.__turno=value 
   
    @apellidos.setter
    def apellidos(self,value):
        self.__apellidos=value  
        
    @nombres.setter
    def nombres(self,value):
        self.__nombres=value 
        
    @login.setter
    def login(self,value):
        self.__login=value  
        
    @password.setter
    def password(self,value):
        self.__password=value 
    
    def Agregar(self):
        try: 
            self.codigo=int(input("Ingrese codigo: "))
            self.dni=input("Ingrese DNI: ")
            self.tipo=int(input("Ingrese tipo de empleado: si es enfermera=01, si es tecnico de enfermeria=02 y si es doctor=03: "))
            self.turno=int(input("Ingrese turno de empleado: si es turno de 7am a 7pm =01y si es turno de 7pm a 7am=02: "))
            self.apellidos=input("Ingrese Apellidos: ")
            self.nombres=input("Ingrese Nombres: ")
            self.login=input("Ingrese login o usuario: ")
            self.password=input("Ingrese contraseña: ")
        except ValueError as error:
            print(f"Ingrese solo datos validos: {error}")
        except Exception as error:
            print("Error al ingresar los valores")
        else:
            print("Sin errores")

    def Actualizar(self, codigo):
        cont = 0
        for empleado in empleados:
            if empleado[0] == codigo:
                self.Agregar()
                new_empleado = self.Obtener()
                empleados[cont] = new_empleado
            cont = cont + 1

    def Eliminar(self, codigo):
        for empleado in empleados:
            if empleado[0] == codigo:
                empleados.remove(empleado)
                print("Empleado eliminado correctamente")
                break
        
    def Listar(self):
        print("Listado de Empleados")
        for empleado in empleados:
            print(empleado)

    def Obtener(self):
        return self.codigo,self.dni,self.tipo,self.turno,self.apellidos,self.nombres,self.login,self.password
        
print("Mantemineto de Empleados")

while True:    
    print("Seleccione una opcion")
    print("1.- Agregar")
    print("2.- Actualizar")
    print("3.- Eliminar")
    print("4.- Listar")
    print("0.- Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        e1=Empleado()
        e1.Agregar()
        empleado = e1.Obtener()
        empleados.append(empleado)
        print("Empleado agregador correctamente", empleados[0])
    elif opcion == 2:
        e1=Empleado()
        e1.Listar()
        codigo = int(input("Ingrese el codigo del empleado a actualizar: "))
        e1.Actualizar(codigo)
    elif opcion == 3:
        e1=Empleado()
        e1.Listar()
        codigo = int(input("Ingrese el codigo del empleado a actualizar: "))
        e1.Eliminar(codigo)
    elif opcion == 4:
        e1=Empleado()
        e1.Listar()
    elif opcion == 0:
        print("Ha seleccionado la opción Salir.")
        break