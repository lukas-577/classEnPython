from os import system
from classes.productos import productos
from DAO import DAO


class DigitarDatosProducto:

    d = DAO()
    productos = productos()

    def digitardatosdeproducto(self):
        system("cls")
        from funciones.menu import Menu
        # codProducto = int(input("Digite El ID del Producto : "))
        cantidad = int(input("digite cantidad del Producto : "))
        nombre = input("Digite El Nombre Del Producto : ")
        precio_unitario = float(input("Ingrese el valor del producto : "))
        codProducto = int(input("Digite El codigo del Producto : "))
        total = (precio_unitario*cantidad)
        iva = (total*self.productos.getiva())
        total_final = (total+self.productos.getiva())
        # codProducto = self.d.comprobarcodigoproducto(20, 'Codigo')
        validacion = self.d.buscarproducto(codProducto)
        if validacion == True:
            print("El producto ingresado ya se encuentra registrado!")

            # nombre = self.__validarTexto(20, 'el nombre')
            # cantidad = self.__validarNumeros(20, ' la cantidad')
            # precio_unitario = self.__validarNumeros(500, 5000, 'el precio')
        else:
            pro = productos()
            pro.setcodProducto(codProducto)
            pro.setnombre(nombre.upper())
            pro.setprecio_unitario(precio_unitario)
            pro.setiva(iva)
            pro.setcantidad(cantidad)
            pro.settotal(total)
            pro.settotal_final(total_final)
            # pro.set(self.sesion.getid_usuario())
            self.d.agregarproducto(pro)
            print("\n--- Producto ("+nombre +
                  ") Registrado Correctamente!! ---", end="\n\n")
            system("pause")
            system("cls")
        menu = Menu()
        menu.menu()
