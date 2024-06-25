class ventas:
    __idventa = 0
    __fecha = ""
    __tipo_documento = 0
    __idvendedor = 0
    __total_neto = 0
    __total_iva = 0.19
    __total_final = 0

    def __init__(self):
        pass

    def getidventa(self):
        return self.__idventa
    
    def setidventa(self, idventa):
        self.__idventa = idventa
        
    def getfecha(self):
        return self.__fecha
    
    def setfecha(self, fecha):
        self.__fecha = fecha

    def gettipo_documento(self):
        return self.__tipo_documento
    
    def settipo_documento(self, tipo_documento):
        self.__tipo_documento = tipo_documento

    def getidvendedor(self):
        return self.__idvendedor
    
    def setidvendedor(self, idvendedor):
        self.__idvendedor = idvendedor

    def gettotal_neto(self):
        return self.__total_neto
    
    def settotal_neto(self, total_neto):
        self.__total_neto = total_neto


    def gettotal_iva(self):
        return self.__total_iva
    
    def settotal_iva(self, total_iva):
        self.__total_iva = total_iva

    def gettotal_final(self):
        return self.__total_final
    
    def settotal_final(self, total_final):
        self.__total_final = total_final