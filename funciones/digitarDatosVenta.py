from os import system
from datetime import datetime
from classes.ventas import ventas
from classes.detallesventas import detallesventas
from classes.factura import factura
from classes.usuario import usuario
from DAO import DAO


class DigitarDatosVenta:
    def __init__(self):
        self.sesion = usuario()
        self.d = DAO()

    def digitardatosdeventas(self):
        system("cls")

        tipo_documento = input(
            "Digite tipo de documento (Boleta o Factura) : ")
        id_vendedor = self.sesion.getid_usuario()

        ven = ventas()

        fecha_actual = datetime.now()

        ven.setfecha(fecha_actual)
        ven.settipo_documento(tipo_documento)
        ven.setidvendedor(id_vendedor)

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
        self.d.agregarventa(ven)

        # idventagenerada = rs[0]

        det = detallesventas()
        # det.setid_venta(idventagenerada)
        det.setcantidad(cantidad)
        det.setprecio_unitario(precio_unitario)
        det.settotal(total)

        # Se inserta en la tabla "ventas".
        self.d.agregardetallesventas(det)

        system("cls")
        print("--- VENTA GENERADA!! ---", end="\n")
        print("--- DETALLE DE VENTA OK!! ---", end="\n\n")

        system("pause")
        # menu = Menu()
        # menu.menu()

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
        # self.menu()
