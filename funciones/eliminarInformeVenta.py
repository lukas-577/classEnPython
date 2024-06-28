from os import system
from DAO import DAO
from funciones.digitarInformeDeVentas import informe


def eliminarinformedeventas():
    from funciones.menu import menu
    d = DAO()
    try:
        # idinforme = d.comprobarcodigoinformeventas("id")
        validacion = d.buscarinformedeventas(informe.getidinforme())
        if validacion == True:
            d.eliminarinformedeventas(informe.getidinforme())
            print("\n--- Informe de Ventas Eliminado Correctamente!! ---")
        else:
            print("\n--- Informe de Ventas No Encontrado!! ---")
    except:
        print("\n--- Error Al Buscar el informe!! ---")
        system("pause")
        menu()
