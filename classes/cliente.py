class cliente:
    __id_cliente = 0
    __razon_social = 0
    __rut = 0
    __giro = ""
    __direccion = ""

    def __init__(self):
        pass

    def getid_cliente(self):
        return self.__id_cliente
    
    def setid_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def getrazonsocial(self):
        return self.__razon_social
    
    def setrazonsocial(self, razonsocial):
        self.__razon_social = razonsocial

    def getrut(self):
        return self.__rut
    
    def setrut(self, rut):
        self.__rut = rut
    
    def getgiro(self):
        return self.__giro
    
    def setgiro(self, giro):
        self.__giro = giro

    def getdireccion(self):
        return self.__direccion
    
    def setdireccion(self, direccion):
        self.__direccion = direccion