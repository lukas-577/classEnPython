from os import system
from classes.productos import productos
from DAO import DAO


d = DAO()
pro = productos()


def digitardatosdeproducto():
    try:
        from funciones.menu import menu
        system("cls")
        cantidad = int(input("Digite cantidad del Producto: "))
        nombre = input("Digite El Nombre Del Producto: ")
        precio_unitario = float(input("Ingrese el valor del producto: "))
        codProducto = int(input("Digite El codigo del Producto: "))

        total = precio_unitario * cantidad
        iva = (total * pro.getiva()) / 100
        total_final = total + iva

        validacion = d.buscarproducto(codProducto)
        if validacion:
            print("El producto ingresado ya se encuentra registrado!")
        else:

            pro.setcodProducto(codProducto)
            pro.setnombre(nombre.upper())
            pro.setprecio_unitario(precio_unitario)
            pro.setiva(iva)
            pro.setcantidad(cantidad)
            pro.settotal(total)
            pro.settotal_final(total_final)

            # pro.set(self.sesion.getid_usuario())
            id_producto = d.agregarproducto(pro)
            pro.setidProducto(id_producto)
            print("id_producto", pro.getidProducto())
            print("\n--- Producto (" + nombre +
                  ") Registrado Correctamente!! ---", end="\n\n")
            system("pause")

            system("cls")

        menu()
    except Exception as e:
        print(f"\n--- Error Al Ingresar Datos Del Producto: {e} ---")
        system("pause")
        system("cls")
