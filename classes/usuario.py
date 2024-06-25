class usuario:
    __id_usuario = 0
    __nombre_usuario = ""
    __contrasena = ""
    __tipo_usuario = ""

    def __init__(self):
        pass

    def getid_usuario(self):
        return self.__id_usuario
    
    def setid_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def getnombre_usuario(self):
        return self.__nombre_usuario
    
    def setnombre_usuario(self, __nombre_usuario):
        self.__nombre_usuario = __nombre_usuario

    def getcontrasena(self):
        return self.__contrasena
    
    def setcontrasena(self, __contrasena):
        self.__contrasena = __contrasena
    
    def getipo_usuario(self):
        return self.__tipo_usuario
    
    def settipo_usuario(self, __tipo_usuario):
        self.__tipo_usuario = __tipo_usuario