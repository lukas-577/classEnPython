class informe_ventas:
    __idinforme = 0
    __cantidad_ventas_boleta = 0
    __monto_boletas_neto = 0
    __monto_boletas_iva = 0
    __monto_boletas_total = 0
    __cantidad_facturas = 0
    __monto_facturas_neto = 0
    __monto_facturas_iva = 0
    __monto_facturas_total = 0

    def __init__(self):
        pass

    def getidinforme(self):
        return self.__idinforme
    
    def setidinforme(self, idinforme):
        self.__idinforme= idinforme

    def getcantidad_ventas_boletas(self):
        return self.__cantidad_ventas_boleta
    
    def setcantidad_ventas_boletas(self, cantidad_ventas_boletas):
        self.__cantidad_ventas_boleta = cantidad_ventas_boletas

    def getmonto_boletas_neto(self):
        return self.__monto_boletas_neto
    
    def setmonto_boletas_neto(self, monto_boletas_neto):
        self.__monto_boletas_neto = monto_boletas_neto

    def getmonto_boletas_iva(self):
        return self.__monto_boletas_iva
    
    def setmonto_boletas_iva(self, monto_boletas_iva):
        self.__monto_boletas_iva = monto_boletas_iva
        
    def getmonto_boletas_total(self):
        return self.__monto_boletas_total
    
    def setmonto_boletas_total(self, monto_boletas_total):
        self.__monto_boletas_total = monto_boletas_total

    def getcantidad_facturas(self):
        return self.__cantidad_facturas
    
    def setcantidad_facturas(self, cantidad_facturas):
        self.__cantidad_facturas = cantidad_facturas

    def getmonto_facturas_neto(self):
        return self.__monto_facturas_neto
    
    def setmonto_facturas_neto(self, monto_facturas_neto):
        self.__monto_facturas_neto = monto_facturas_neto

    def getmonto_facturas_iva(self):
        return self.__monto_facturas_iva
    
    def setmonto_facturas_iva(self,monto_facturas_iva):
        self.__monto_facturas_iva = monto_facturas_iva

    def getmonto_facturas_iva(self):
        return self.__monto_facturas_total
    
    def setmonto_facturas_iva(self,monto_facturas_total):
        self.__monto_facturas_total = monto_facturas_total