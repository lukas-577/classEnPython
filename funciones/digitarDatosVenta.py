from os import system
from datetime import datetime
from classes.ventas import ventas
from classes.detallesventas import detallesventas
from classes.factura import factura
from classes.usuario import usuario
from funciones.digitarDatosProducto import pro
from DAO import DAO

det = detallesventas()
ven = ventas()


def digitardatosdeventas():
    # importar localmente para evitar errores de importación circular
    from funciones.iniciarSeccion import sesion
    from funciones.menu import menu

    d = DAO()

    system("cls")

    tipo_documento = input(
        "Digite tipo de documento (Boleta o Factura) : ")
    id_vendedor = sesion.getid_usuario()
    print("id_vendedor", id_vendedor)

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
    rs = d.agregarventa(ven)

    idventagenerada = rs[0]
    print("id venta generada Usalo al ingresar la factura", idventagenerada)

    id_producto = pro.getidProducto()
    print("id_producto", id_producto)

    det.setid_producto(id_producto)
    det.setid_venta(idventagenerada)
    det.setcantidad(cantidad)
    det.setprecio_unitario(precio_unitario)
    det.settotal(total)

    # Se inserta en la tabla "ventas".
    rescienGenerado = d.agregardetallesventas(det)

    det.setiddetalle(rescienGenerado[0])

    system("cls")
    print("--- VENTA GENERADA!! ---", end="\n")
    print("--- DETALLE DE VENTA OK!! ---", end="\n\n")

    system("pause")
    # menu = Menu()
    # menu.menu()

    # idfactura = int(input("ingrese id de factura"))
    print("\n--- Ingrese los datos de la factura ---\n")
    idventa = int(input("ingrese id de venta generada : "))
    idcliente = int(input("ingrese id cliente: "))
    fac = factura()
    # fac.setidfactura(idfactura)
    fac.setidventa(idventa)
    fac.setidcliente(idcliente)

    d.agregarfactura(fac)

    system("cls")
    print(f"\n--- Ejercicio ({idventa}) Registrado Correctamente!! ---\n")
    system("pause")
    menu()
