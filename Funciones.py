from classes.usuario import usuario
from classes.productos import productos
from classes.ventas import ventas
from classes.factura import factura
from classes.informe_ventas import informe_ventas
from classes.detallesventas import detallesventas
from DAO import DAO
from os import system
import os
import getpass

from datetime import datetime


class Funciones:

    d = DAO()
    sesion = usuario()

    def __init__(self):
        pass

# --------------------------------------------------------------------

    def menuInicial(self):
        while True:
            try:
                system("cls")
                print("MENU ")
                print("1.Iniciar Sesion")
                print("2.Registrarse")
                print("3.Salir")
                op = int(input("Digite Una opcion : "))
                if op == 1:
                    self.__iniciarsesion()
                elif op == 2:
                    self.__crearCuenta()
                elif op == 3:
                    self.__salir()
                    break
            except:
                print("Error Al Digitar Opcion")
                system("pause")

# --------------------------------------------------------------------

    def __iniciarsesion(self):
        while True:
            try:
                system("cls")
                print("--- LOGIN ---")
                nombre_usuario = input("Digite El Nombre de Usuario : ")

                if len(nombre_usuario) < 1 or len(nombre_usuario) > 10:
                    print("\n--- Debe Tener Entre 1 y 10 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar Nombre De Usuario!! ---")
                system("pause")

        while True:
            try:
                system("cls")
                print("--- LOGIN ---")
                contrasena = getpass.getpass(
                    "Digite La Contraseña Del Usuario ("+nombre_usuario.upper()+") : ")
                if len(contrasena) < 1 or len(contrasena) > 50:
                    print("\n--- Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except:
                print("\n--- Error Al Ingresar Contraseña (Login)!! ---")
                system("pause")

        system("cls")
        # --- Continuar Codificación ---
        r = self.d.iniciarSesion(nombre_usuario, contrasena)
        if r is None:
            print("\n---Error de Usuario y/o Contraseña!!", end="\n\n")
            system("pause")
            self.menuInicial()
        else:
            self.sesion.setid_usuario(r[0])
            self.sesion.setnombre_usuario(r[1])
            self.sesion.setcontrasena(r[2])
            self.sesion.settipo_usuario(r[3])
            print(
                f"\n--- Bienvenido Usuario {self.sesion.getnombre_usuario().upper()} !! ---", end="\n\n")
            system("pause")
            self.menu()


# --------------------------------------------------------------------

    def __crearCuenta(self):
        while True:
            try:
                system("cls")
                nombre = input("Digite El Nombre del Usuario a Registrar : ")
                if len(nombre.strip()) < 1 or len(nombre.strip()) > 10:
                    print("\n--- El Nombre Debe Tener Entre 1 y 0 Caracteres!! ---")
                    system("pause")
                else:
                    r = self.d.comprobarNombreUsuario(nombre)
                    if r is not None:
                        print("\n--- El Nombre de Usuario (",
                              nombre, ") Ya Existe!! ---\n")
                        system("pause")
                    else:
                        break
            except:
                print("\n--- Error Al Intentar Almacenar El Nombre De Usuario!! ---")
                system("pause")

        while True:
            try:
                system("cls")
                contrasena = getpass.getpass(
                    "Digite La Password Del Usuario ("+str(nombre.upper())+") : ")
                if len(contrasena.strip()) < 1 or len(contrasena.strip()) > 10:
                    print("\n--- Debe Tener Entre 1 y 10 Caracteres!! ---\n")
                    system("pause")
                else:
                    pas2 = getpass.getpass(
                        "Repita La Password Del Usuario ("+str(nombre.upper())+") : ")
                    if contrasena != pas2:
                        print("\n--- Las Contrasenas No Coinciden!! ---\n")
                        system("pause")
                    else:
                        break
            except:
                print("\n--- Error Al Intentar Almacenar La Password!! ---")
                system("pause")

        u = usuario()
        u.setnombre_usuario(nombre.upper())
        u.setcontrasena(contrasena)

        self.d.agregarUsuario(u)
        system("cls")
        print("--- Cuenta de Usuario Creada Correctamente!! ---", end="\n\n")
        system("pause")
        self.menuInicial()

# --------------------------------------------------------------------

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
                self.__digitardatosdeproducto()
            if op == 2:
                self.__digitardatosdeventas()

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
        except:
            print("\n--- Error De Opcion !! ---")
            system("pause")
            self.menu()

# --------------------------------------------------------------------

    def __digitardatosdeproducto(self):
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

# --------------------------------------------------

    def __digitardatosdeventas(self):
        system("cls")

        # No se digita el "idventa" porque en su tabla lo dejó auto_increment.
        # idventa        = int(input("Digite El ID de la venta : "))

        tipo_documento = input(
            "Digite tipo de documento (Boleta o Factura) : ")
        id_vendedor = self.sesion.getid_usuario()

        ven = ventas()

        fecha_actual = datetime.now()

        ven.setfecha(fecha_actual)
        ven.settipo_documento(tipo_documento)
        ven.setidvendedor(id_vendedor)

        # No se digita el "id_detalle" porque en su tabla lo dejó auto_increment.
        # id_detalle = int(input("Digite El id del detalle de la venta: "))

        # este id_venta no se digita, sino que, se debe recuperar después de insertar en la tabla "ventas".
        # id_venta = int(input("digite id de venta del Producto"))

        id_producto = int(input("Digite el ID del Producto a Agregar : "))
        cantidad = int(input("Digite la Cantidad de Productos a Agregar : "))
        precio_unitario = int(input("Digite el Precio del Prodcuto : "))
        total = precio_unitario * cantidad

        total_neto = total
        total_iva = total_neto * 0.19
        total_final = total_neto + total_iva

        ven.settotal_neto(total_neto)
        ven.settotal_iva(total_iva)
        ven.settotal_final(total_final)

        # Se inserta en la tabla "ventas".
        rs = self.d.agregarventa(ven)

        idventagenerada = rs[0]

        det = detallesventas()
        det.setid_venta(idventagenerada)
        det.setid_producto(id_producto)
        det.setcantidad(cantidad)
        det.setprecio_unitario(precio_unitario)
        det.settotal(total)

        # Se inserta en la tabla "ventas".
        self.d.agregardetallesventas(det)

        system("cls")
        print("--- VENTA GENERADA!! ---", end="\n")
        print("--- DETALLE DE VENTA OK!! ---", end="\n\n")

        system("pause")
        self.menu()

        idfactura = int(input("ingrese id de factura"))
        idventa = int(input("ingrese id de venta"))
        idcliente = int(input("ingrese id cliente"))
        fac = factura()
        fac.setidfactura(idfactura)
        fac.setidventa(idventa)
        fac.setidcliente(idcliente)

        self.d.agregarfactura(fac)
        fac.setid_usuario(self.sesion.getid_usuario())

        system("cls")
        print("\n--- Ejercicio ("+idventa +
              ") Registrado Correctamente!! ---", end="\n\n")
        system("pause")
        self.menu()


# --------------------------------------------------------------------
# ------------------------------------------------------------------

    def __digitarinformedeventas(self):
        system("cls")
        idinforme = int(input("Digite codigo de informe de ventas  : "))
        cantidad_ventas_boleta = int(input("digite cantidad del Producto"))
        monto_boletas_neto = input("Digite razon social de la factura : ")
        monto_boletas_iva = int(input("Digite El rut de la factura   : "))
        cantidad_facturas = int(input("digite el giro de la factura"))
        monto_facturas_neto = ("Digite direccion de la factura : ")
        monto_facturas_iva = int(input("Digite numero de factura  : "))

        idinforme = self.d.comprobarcodigoinformeventas(20, 'Codigo')
        validacion = self.d.buscarinformedeventas(idinforme)
        if validacion == True:
            print("la venta  ingresada ya se encuentra registrado!")
        else:
            cantidad_ventas_boleta = self.__validarNumeros(20, 'el nombre')
            monto_boletas_neto = self.__validarNumeros(20, ' la cantidad')
            monto_boletas_iva = self.__validarNumeros(500, 5000, 'el precio')
            cantidad_facturas = self.__validarNumeros(20, ' la cantidad')
            monto_facturas_neto = self.__validarNumeros(500, 5000, 'el precio')
            monto_facturas_iva = self.__validarNumeros(500, 5000, 'el precio')

        i = informe_ventas()
        i.setidinforme(idinforme)
        i.setcantidad_ventas_boletas(cantidad_ventas_boleta)
        i.setmonto_boletas_neto(monto_boletas_neto)
        i.setmonto_boletas_iva(monto_boletas_iva)
        i.setcantidad_facturas(cantidad_facturas)
        i.setmonto_facturas_neto(monto_facturas_neto)
        i.setmonto_facturas_iva(monto_facturas_iva)

        i.setid_usuario(self.sesion.getid_usuario())

        self.d.agregarinformedeventas(i)
        system("cls")
        print("\n--- Informe de ventas ("+idinforme +
              ") Registrado Correctamente!! ---", end="\n\n")
        system("pause")
        self.menu()

    def __eliminarproducto(self):
        try:
            idproducto = self.d.comprobarcodigoproducto("codigo")
            validacion = self.d.buscarproducto(idproducto)
            if validacion == True:
                self.d.eliminarproducto(idproducto)
            print("eliminar producto")
        except:
            print("\n--- Error Al Buscar el producto!! ---")
            system("pause")
            self.menu()

    def eliminarventa(self):
        try:
            idventa = self.d.comprobarcodigoventa("codigo")
            validacion = self.d.buscarventa(idventa)
            if validacion == True:
                self.d.eliminarventa(idventa)
            print("eliminar venta")
        except:
            print("\n--- Error Al Buscar la venta!! ---")
            system("pause")
            self.menu()

    def __eliminardetallesdeventas(self):
        try:
            iddetalle = self.d.comprobarcodigodetalleventas("id")
            validacion = self.d.buscardetatallesdeventas(iddetalle)
            if validacion == True:
                self.d.eliminarinformedeventas(iddetalle)
            print("eliminar detalle")
        except:
            print("\n--- Error Al Buscar el detalle!! ---")
            system("pause")
            self.menu()

# --------------------------------------------------------------------

    def __eliminarinformedeventas(self):
        try:
            idinforme = self.d.comprobarcodigoinformeventas("id")
            validacion = self.d.buscarinformedeventas(idinforme)
            if validacion == True:
                self.d.eliminarinformedeventas(idinforme)
            print("eliminar informe")
        except:
            print("\n--- Error Al Buscar el informe!! ---")
            system("pause")
            self.menu()

# --------------------------------------------------------------------

    def __listarproducto(self):
        system("cls")
        rs = self.d.obtenerproducto()
        print('---LISTA DE productos---')
        for x in rs:
            print('CODIGO:', x[0])
            print('NOMBRE:', x[1])
            print('--------------')

        system("pause")
        self.menu()

    def __listarventas(self):
        system("cls")
        rs = self.d.obtenerventas()
        print('---LISTA DE ventas---')
        for x in rs:
            print('CODIGO:', x[0])
            print('NOMBRE:', x[1])
            print('--------------')

        system("pause")
        self.menu()

    def __listardetalles_ventas(self):
        system("cls")
        rs = self.d.obtenerdetallesventas()
        print('---LISTA DE ventas---')
        for x in rs:
            print('CODIGO:', x[0])
            print('NOMBRE:', x[1])
            print('--------------')

        system("pause")
        self.menu()

    def __listarinforme_ventas(self):
        system("cls")
        rs = self.d.obtenerinformedeventas()
        print('---LISTA DE informe de ventas---')
        for x in rs:
            print('CODIGO:', x[0])
            print('NOMBRE:', x[1])
            print('--------------')

        system("pause")
        self.menu()

    def __salir(self):
        system("cls")
        print("-------------------")
        print("--- OK. Adios!! ---")
        print("-------------------")
        system("pause")

# --------------------------------------------------------------------
