from Funciones import Funciones
from funciones.menuInicial import MenuInicial
from funciones.digitarDatosProducto import DigitarDatosProducto


class Principal:

    f = Funciones()
    menu = MenuInicial()
    digitar = DigitarDatosProducto()

    def ejecutarPrograma(self):
        self.digitar.digitardatosdeproducto()

# -------------------------------------------------------------------


p = Principal()
p.ejecutarPrograma()
