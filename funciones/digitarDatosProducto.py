from os import system
from classes.productos import productos


class DigitarDatosProducto:
    def digitardatosdeproducto(self):
        system("cls")

        idproducto = int(input("Digite El ID del Producto : "))
        nombre = input("Digite El Nombre Del Producto : ")
        precio_unitario = float(input("Ingrese el valor del producto : "))
        cantidad = int(input("digite cantidad del Producto"))
        total = (precio_unitario*cantidad)
        iva = (total*iva)
        total_final = (total+iva)

        idproducto = self.d.comprobarcodigoproducto(20, 'Codigo')
        validacion = self.d.buscarproducto(idproducto)
        if validacion == True:
            print("El producto ingresado ya se encuentra registrado!")
        else:
            nombre = self.__validarTexto(20, 'el nombre')
            cantidad = self.__validarNumeros(20, ' la cantidad')
            precio_unitario = self.__validarNumeros(500, 5000, 'el precio')

        pro = productos()
        pro.setidproducto(idproducto)
        pro.setnombre(nombre.upper())
        pro.setprecio_unitario(precio_unitario)
        pro.setiva(iva)
        pro.setcantidad(cantidad)
        pro.settotal(total)
        pro.settotal_final(total_final)
        pro.setid_usuario(self.sesion.getid_usuario())
        self.d.agregarproducto(pro)
        system("cls")
        print("\n--- Producto ("+nombre+") Registrado Correctamente!! ---", end="\n\n")
        system("pause")
        self.menu()
