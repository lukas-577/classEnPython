from os import system
from DAO import DAO


def eliminarventa():
    from funciones.menu import menu
    from funciones.digitarDatosVenta import ven
    d = DAO()

    try:
        # idventa = d.comprobarcodigoventa("codigo")
        validacion = d.buscarventa(ven.getidventa())
        if validacion == True:
            d.eliminarventa(ven.getidventa())
            print("\n--- Venta Eliminada Correctamente!! ---")
        else:
            print("\n--- Venta No Encontrada!! ---")
    except:
        print("\n--- Error Al Buscar la venta!! ---")
        system("pause")
        menu()
