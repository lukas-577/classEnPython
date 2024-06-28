from os import system
from DAO import DAO


def eliminardetallesdeventas():
    from funciones.menu import menu
    from funciones.digitarDatosVenta import det
    d = DAO()

    try:
        # iddetalle = d.comprobarcodigodetalleventas("id")
        print(det.getiddetalle())
        validacion = d.buscardetatallesdeventas(det.getiddetalle())
        if validacion == True:
            d.eliminardetallesventas(det.getiddetalle())
            print("Detalle Eliminado")
        else:
            print("\n--- Detalle No Encontrado!! ---")
        menu()
    except:
        print("\n--- Error Al Buscar el detalle!! ---")
        system("pause")
        menu()
