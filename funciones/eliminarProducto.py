from os import system
from DAO import DAO


def eliminarproducto():
    from funciones.menu import menu
    from funciones.digitarDatosProducto import pro
    d = DAO()
    try:
        # idproducto = d.comprobarcodigoproducto("codigo")
        validacion = d.buscarproducto(pro.getidProducto())
        if validacion == True:
            d.eliminarproducto(pro.getidProducto())
            print("Producto Eliminado" + str(pro.getidProducto()))
        else:
            print("\n--- Producto No Encontrado!! ---")
        system("pause")
        menu()
    except Exception as e:
        print(f"\n--- Error Al Buscar el producto!! --- {str(e)}")
        system("pause")
        menu()
