from funciones.menuInicial import menuInicial
from funciones.digitarDatosProducto import digitardatosdeproducto
from funciones.digitarDatosVenta import digitardatosdeventas


def ejecutarPrograma():
    # Aquí se llama sólo al menú inicial, que manejará el flujo
    # menuInicial()
    digitardatosdeproducto()
    # digitardatosdeventas()


if __name__ == "__main__":
    ejecutarPrograma()
