class usuario:
    def __init__(self):
        self.__id_usuario = 0
        self.__nombre_usuario = ""
        self.__contrasena = ""
        self.__tipo_usuario = ""

    def getid_usuario(self):
        return self.__id_usuario

    def setid_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def getnombre_usuario(self):
        return self.__nombre_usuario

    def setnombre_usuario(self, nombre_usuario):
        self.__nombre_usuario = nombre_usuario

    def getcontrasena(self):
        return self.__contrasena

    def setcontrasena(self, contrasena):
        self.__contrasena = contrasena

    def gettipo_usuario(self):
        return self.__tipo_usuario

    def settipo_usuario(self, tipo_usuario):
        self.__tipo_usuario = tipo_usuario


# Crear una única instancia global
usuario_actual = usuario()
