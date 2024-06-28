from os import system
from classes.informe_ventas import informe_ventas
from DAO import DAO
from datetime import datetime


def digitarinformedeventas():
    d = DAO()
    fecha_actual = datetime.now()
    system("cls")

    idinforme = int(input("Digite código de informe de venta: "))
    cantidad_ventas_boleta = int(
        input("Ingrese la cantidad de ventas por boleta: "))
    monto_boletas_neto = float(input("Ingrese el monto neto de las boletas: "))
    monto_boletas_iva = float(
        input("Ingrese el monto de IVA de las boletas: "))
    monto_boletas_total = float(
        input("Ingrese el monto total de las boletas: "))
    cantidad_facturas = int(input("Ingrese la cantidad de facturas: "))
    monto_facturas_neto = float(
        input("Ingrese el monto neto de las facturas: "))
    monto_facturas_iva = float(
        input("Ingrese el monto de IVA de las facturas: "))
    monto_facturas_total = float(
        input("Ingrese el monto total de las facturas: "))
    id_vendedor = int(input("Ingrese el ID del vendedor: "))

    validacion = d.buscarinformedeventas(idinforme)
    if validacion:
        print("El informe de venta ingresado ya se encuentra registrado!")
    else:
        informe = informe_ventas()
        informe.setidinforme(idinforme)
        informe.setcantidad_ventas_boletas(cantidad_ventas_boleta)
        informe.setmonto_boletas_neto(monto_boletas_neto)
        informe.setmonto_boletas_iva(monto_boletas_iva)
        informe.setmonto_boletas_total(monto_boletas_total)
        informe.setcantidad_facturas(cantidad_facturas)
        informe.setmonto_facturas_neto(monto_facturas_neto)
        informe.setmonto_facturas_iva(monto_facturas_iva)
        informe.setmonto_facturas_total(monto_facturas_total)
        informe.setid_vendedor(id_vendedor)
        # Asumiendo que tienes un método setfecha en tu clase informe_ventas
        informe.setfecha(fecha_actual)

        d.agregarinformedeventas(informe)
        system("cls")
        print(
            f"\n--- Informe de ventas ({idinforme}) Registrado Correctamente!! ---\n")
        system("pause")
