establecimientos = []

class Establecimiento:
    def __init__(self):
        pass
        
    
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
        
    def Agregar(self):
        try: 
            self.__codigo=int(input("Ingrese codigo: "))
            self.__ruc=input("Ingrese DNI: ")
            self.__nombre=input("Ingrese Apellidos: ")
            
        except ValueError as error:
            print(f"Ingrese solo datos validos: {error}")
        except Exception as error:
            print("Error al ingresar los valores")
        else:
            print("Sin errores")

    def Actualizar(self, codigo):
        cont = 0
        for establecimiento in establecimientos:
            if establecimiento[0] == codigo:
                self.Agregar()
                new_establecimiento = self.Obtener()
                establecimientos[cont] = new_establecimiento
            cont = cont + 1

    def Eliminar(self, codigo):
        for establecimiento in establecimientos:
            if establecimiento[0] == codigo:
                establecimientos.remove(establecimiento)
                print("Establecimiento eliminado correctamente")
                break
        
    def Listar(self):
        print("Listado de Establecimientos")
        for establecimiento in establecimientos:
            print(establecimiento)

    def Obtener(self):
        return self.codigo,self.ruc,self.nombre
        
print("Mantemineto de Establecimientos")

while True:    
    print("Seleccione una opcion")
    print("1.- Agregar")
    print("2.- Actualizar")
    print("3.- Eliminar")
    print("4.- Listar")
    print("0.- Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        e1=Establecimiento()
        e1.Agregar()
        establecimiento = e1.Obtener()
        establecimientos.append(establecimiento)
        print("Establecimiento agregado correctamente", establecimientos[0])
    elif opcion == 2:
        e1=Establecimiento()
        e1.Listar()
        codigo = int(input("Ingrese el codigo del establecimiento a actualizar: "))
        e1.Actualizar(codigo)
    elif opcion == 3:
        e1=Establecimiento()
        e1.Listar()
        codigo = int(input("Ingrese el codigo del establecimiento a actualizar: "))
        e1.Eliminar(codigo)
    elif opcion == 4:
        e1=Establecimiento()
        e1.Listar()
    elif opcion == 0:
        print("Ha seleccionado la opción Salir.")
        break
        
    