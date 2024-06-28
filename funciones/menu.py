from os import system
# from classes.usuario import usuario

from funciones.digitarDatosProducto import digitardatosdeproducto
from funciones.digitarDatosVenta import digitardatosdeventas
from funciones.digitarInformeDeVentas import digitarinformedeventas

# Inicializar los objetos necesarios

# sesion = usuario()
# digitar = digitardatosdeproducto()


def menu():
    # importar localmente para evitar errores de importación circular
    from funciones.iniciarSeccion import sesion
    from funciones.digitarDatosProducto import pro
    try:
        system("cls")
        print(f"--- MENU DE {sesion.getnombre_usuario().upper()} ---")
        print(f"--- MENU DE {pro.getidProducto()} ---")
        print("1.Agregar Producto")
        print("2.Generar Ventas")
        print("3.Agregar factura")
        print("4.Agregar informe de ventas ")
        print("5.Agregar detalles de ventas")
        print("6.eliminar producto")
        print("7. eliminar venta")
        print("7.eliminar informedeventas")
        print("8. eliminar detalles de ventas")
        print("9.Cerrar Sesion")
        op = int(input("Digite Una Opcion : "))
        if op == 1:
            digitardatosdeproducto()
            system("pause")
        if op == 2:
            digitardatosdeventas()

        if op == 3:
            digitarinformedeventas()
        # if op == 4:
        #     __eliminarproducto()
        # if op == 5:
        #     __eliminarinformedeventas()
        # if op == 6:
        #     __eliminardetallesdeventas()

        # if op == 7:
        #     __listarproducto
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
