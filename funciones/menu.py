from os import system
from classes.usuario import usuario
from funciones.digitarDatosProducto import DigitarDatosProducto
from funciones.digitarDatosVenta import DigitarDatosVenta


class Menu:

    def __init__(self):
        self.sesion = usuario()
        self.digitar = DigitarDatosProducto()
        self.digitarventa = DigitarDatosVenta()

    def menu(self):
        try:
            system("cls")
            print(f"--- MENU DE {self.sesion.getnombre_usuario().upper()} ---")
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
                self.digitar.digitardatosdeproducto()
            if op == 2:
                self.digitarventa.digitardatosdeventas()

            if op == 3:
                self.__digitarinformedeventas()
            if op == 4:
                self.__eliminarproducto()
            if op == 5:
                self.__eliminarinformedeventas()
            if op == 6:
                self.__eliminardetallesdeventas()

            if op == 7:
                self.__listarproducto
            if op == 8:
                self.__listarventas()
            if op == 9:
                self.__listarinforme_ventas
            if op == 10:
                self.__listardetalles_ventas()
            elif op == 11:
                self.menuInicial()
        except Exception as e:
            print(f"\n--- Error De Opcion !! --- {str(e)}")
            system("pause")
            self.menu_inicial.menuInicial()
