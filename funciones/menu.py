from os import system

from funciones.digitarDatosProducto import digitardatosdeproducto
from funciones.digitarDatosVenta import digitardatosdeventas
from funciones.digitarInformeDeVentas import digitarinformedeventas
from funciones.eliminarProducto import eliminarproducto
from funciones.eliminarDetalleVenta import eliminardetallesdeventas
from funciones.eliminarVenta import eliminarventa
from funciones.eliminarInformeVenta import eliminarinformedeventas


def menu():
    # importar localmente para evitar errores de importación circular
    from funciones.iniciarSeccion import sesion
    from funciones.digitarDatosProducto import pro
    try:
        system("cls")
        print(f"--- MENU DE {sesion.getnombre_usuario().upper()} ---")
        print(f"--- Prodcuto con id:  {pro.getidProducto()} ---")
        print("1.Agregar Producto")
        print("2.Generar Ventas, Agregar factura y Agregar detalles de ventas")
        print("3.Agregar informe de ventas ")
        print("4. eliminar detalles de ventas")
        print("5.eliminar producto depende de eliminar detalles de ventas por fk")
        print("6. eliminar venta")
        print("7.eliminar informedeventas")

        print("9.Cerrar Sesion")
        op = int(input("Digite Una Opcion : "))
        if op == 1:
            digitardatosdeproducto()
            system("pause")
        if op == 2:
            digitardatosdeventas()
            system("pause")

        if op == 3:
            digitarinformedeventas()
            system("pause")
        if op == 4:
            eliminardetallesdeventas()
            system("pause")
        if op == 5:
            eliminarproducto()
            system("pause")
        if op == 6:
            eliminarventa()
            system("pause")
        if op == 7:
            eliminarinformedeventas()
            system("pause")
        # if op == 8:
        #     __listarventas()
        # if op == 9:
        #     __listarinforme_ventas
        # if op == 10:
        #     __listardetalles_ventas()
        # elif op == 11:
        #     self.menuInicial()
    except Exception as e:
        print(f"\n--- Error De Opcion !! --- {str(e)}")
        system("pause")
        # menu_inicial.menuInicial()
