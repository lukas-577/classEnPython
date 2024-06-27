class productos:
    def __init__(self):
        self.__idProducto = 2  # Inicializamos idProducto a 0 al crear el objeto
        self.__codProducto = 0
        self.__nombre = ""
        self.__precio_unitario = 0.0
        self.__cantidad = 0
        self.__iva = 19
        self.__total = 0.0
        self.__total_final = 0.0

    # Métodos getter y setter para idProducto
    def getidProducto(self):
        return self.__idProducto

    def setidProducto(self, idProducto):
        self.__idProducto = idProducto

    # Métodos getter y setter para codProducto
    def getcodProducto(self):
        return self.__codProducto

    def setcodProducto(self, codProducto):
        self.__codProducto = codProducto

    # Métodos getter y setter para nombre
    def getnombre(self):
        return self.__nombre

    def setnombre(self, nombre):
        self.__nombre = nombre

    # Métodos getter y setter para precio_unitario
    def getprecio_unitario(self):
        return self.__precio_unitario

    def setprecio_unitario(self, precio_unitario):
        self.__precio_unitario = precio_unitario

    # Métodos getter y setter para cantidad
    def getcantidad(self):
        return self.__cantidad

    def setcantidad(self, cantidad):
        self.__cantidad = cantidad

    # Métodos getter y setter para iva
    def getiva(self):
        return self.__iva

    def setiva(self, iva):
        self.__iva = iva

    # Métodos getter y setter para total
    def gettotal(self):
        return self.__total

    def settotal(self, total):
        self.__total = total

    # Métodos getter y setter para total_final
    def gettotal_final(self):
        return self.__total_final

    def settotal_final(self, total_final):
        self.__total_final = total_final
