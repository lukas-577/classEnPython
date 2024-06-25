from Funciones import Funciones
from funciones.menuInicial import MenuInicial


class Principal:

    f = Funciones()
    menu = MenuInicial()

    def ejecutarPrograma(self):
        self.menu.menuInicial()

# -------------------------------------------------------------------


p = Principal()
p.ejecutarPrograma()
