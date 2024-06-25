class productos:
    __idproducto: 0
    __nombre= ""
    __precio_unitario = ""
    __cantidad = 0
    __iva = 19
    __total= 0
    __total_final = 0

    def __init__(self):
        pass

    
    def getidproducto(self):
        return self.__idproducto
    
    def setidproducto(self, idproducto):
        self.__idproducto = idproducto

    def getnombre(self):
        return self.__nombre
    
    def setnombre(self, nombre):
        self.__nombre = nombre

    def getprecio_unitario(self):
        return self.__precio_unitario
    
    def setprecio_unitario(self, precio_unitario):
        self.__precio_unitario = precio_unitario


    def getcantidad(self):
        return self.__cantidad
    
    def setcantidad(self, cantidad):
        self.__cantidad = cantidad
    
    
    def getiva(self):
        return self.__iva
    
    def setiva(self, iva):
        self.__iva = iva

    def gettotal(self):
        return self.__total
    
    def settotal(self, total):
        self.__total = total

    def gettotal_final(self):
        return self.__total_final
    
    def settotal_final(self, total_final):
        self.__total_final = total_final