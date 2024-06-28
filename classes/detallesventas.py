
class detallesventas:
    __iddetalle = 0
    __id_venta = 0
    __id_producto = 0
    __cantidad = 0
    __precio_unitario = 0
    __total = 0

    def __init__(self):
        pass

    def getiddetalle(self):
        return self.__iddetalle

    def setiddetalle(self, iddetalle):
        self.__iddetalle = iddetalle

    def getid_venta(self):
        return self.__id_venta

    def setid_venta(self, id_venta):
        self.__id_venta = id_venta

    def getid_producto(self):
        return self.__id_producto

    def setid_producto(self, id_producto):
        self.__id_producto = id_producto

    def getcantidad(self):
        return self.__cantidad

    def setcantidad(self, cantidad):
        self.__cantidad = cantidad

    def getprecio_unitario(self):
        return self.__precio_unitario

    def setprecio_unitario(self, precio_unitario):
        self.__precio_unitario = precio_unitario

    def gettotal(self):
        return self.__total

    def settotal(self, total):
        self.__total = total
