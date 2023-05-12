
class Registro:
    def __init__(self):
        self.__usuario=input("Ingrese su usuario: ")
        self.__password=int(input("Ingrese password de 4 digitos numericos: "))
        assert self.usuario==self.usuario,"Usuario no es correcto"
        assert self.password==self.password,"Password no es correcto"
        print("Datos de ingreso son correctos")
    
    @property
    def usuario(self):
        return self.__usuario
        
    @property
    def password(self):
        return self.__password
        
     
    @usuario.setter
    def usuario(self,value):
        self.__usuario=value  
        
    @password.setter
    def password(self,value):
        self.__password=value 
   
    
    def Imprimir(self):
        print(f"Su usuario para ingresar al sistema es:{self.usuario}")
        print(f"Su password de seguridad es: {self.password}")
        
        
e1=Registro()
e1.Imprimir()
