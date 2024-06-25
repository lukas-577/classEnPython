class factura:
    __idfactura = 0
    __idventa = 0
    __idcliente = 0

    def __init__(self):
        pass

    def getidfactura(self):
        return self.__idfactura
    
    def setidfactura(self, idfactura):
        self.__idfactura = idfactura

    def getidventa(self):
        return self.__idventa
    
    def setidventa(self, idventa):
        self.__idventa = idventa

    def getidcliente(self):
        return self.__idcliente
    
    def setidcliente(self, idcliente):
        self.__idcliente = idcliente

