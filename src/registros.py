registros = []

class Registro:
    def __init__(self):
        pass
       
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

    def Agregar(self):
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
        
    def Actualizar(self, codigo):
        cont = 0
        for registro in registros:
            if registro[0] == codigo:
                self.Agregar()
                new_establecimiento = self.Obtener()
                registros[cont] = new_establecimiento
            cont = cont + 1

    def Eliminar(self, codigo):
        for registro in registros:
            if registro[0] == codigo:
                registros.remove(registro)
                print("Registro eliminado correctamente")
                break
        
    def Listar(self):
        print("Listado de Registro")
        for registro in registros:
            print(registro)

    def Obtener(self):
        return self.codigo_establecimiento,self.codigo_empleado,self.codigo_vacunado,self.codigo_vacuna,self.nombre_establecimiento,self.nombre_empleado,self.nombre_vacunado
        
print("Registro de Vacunacion")

while True:    
    print("Seleccione una opcion")
    print("1.- Agregar")
    print("2.- Actualizar")
    print("3.- Eliminar")
    print("4.- Listar")
    print("0.- Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        r1=Registro()
        r1.Agregar()
        registro = r1.Obtener()
        registros.append(registro)
        print("Registro de Vacunacion Correcta", registros[0])
    elif opcion == 2:
        r1=Registro()
        r1.Listar()
        codigo = int(input("Ingrese el codigo del Establecimiento a actualizar: "))
        r1.Actualizar(codigo)
    elif opcion == 3:
        r1=Registro()
        r1.Listar()
        codigo = int(input("Ingrese el codigo del Establecimiento a actualizar: "))
        r1.Eliminar(codigo)
    elif opcion == 4:
        r1=Registro()
        r1.Listar()
    elif opcion == 0:
        print("Ha seleccionado la opción Salir.")
        break                   
        
        
