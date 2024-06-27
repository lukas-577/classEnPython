from Funciones import Funciones
from funciones.menuInicial import MenuInicial
from funciones.digitarDatosProducto import DigitarDatosProducto
from funciones.digitarDatosVenta import DigitarDatosVenta


class Principal:

    f = Funciones()
    menu = MenuInicial()
    digitar = DigitarDatosProducto()
    venta = DigitarDatosVenta()

    def ejecutarPrograma(self):
        # self.digitar.digitardatosdeproducto()
        self.menu.menuInicial()
        # self.venta.digitardatosdeventas()
# -------------------------------------------------------------------


p = Principal()
p.ejecutarPrograma()
