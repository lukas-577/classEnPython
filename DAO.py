from classes.usuario import usuario
from classes.productos import productos
from classes.detallesventas import detallesventas
from classes.factura import factura
from classes.ventas import ventas
from classes.cliente import cliente
from classes.informe_ventas import informe_ventas
from os import system
import pymysql


class DAO:

    def __init__(self):
        pass

# ----------------------------------------------------------------------

    def conectar(self):
        try:
            self.con = pymysql.connect(
                host="localhost",
                user="root",
                port=3309,
                password="123456",
                db="bd_sistema"
            )
            self.cursor = self.con.cursor()
            print("Conexión exitosa a MySQL")
        except pymysql.Error as e:
            print(f"Error de conexión a MySQL: {e}")

# ----------------------------------------------------------------------

    def desconectar(self):
        self.con.close()

# ----------------------------------------------------------------------

    def iniciarSesion(self, nom, pas):
        try:
            self.conectar()
            sql = "select * from usuarios where Nombre_Usuario=%s and Contrasena=%s"
            val = (nom, pas)
            self.cursor.execute(sql, val)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Iniciar Sesion (DAO)!! ---", end="\n\n")
            system("pause")

# ----------------------------------------------------------------------

    def comprobarNombreUsuario(self, nom):
        try:
            self.conectar()
            sql = "select nom_usu from usuarios where nom_usu=%s"
            self.cursor.execute(sql, nom)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print(
                "\n--- Error Al Comprobar Nombre Del Usuario a Registrar (DAO)!! ---", end="\n\n")
            system("pause")

# ----------------------------------------------------------------------

    def agregarUsuario(self, u):
        try:
            self.conectar()
            sql = "insert into usuarios (nom_usu, pas_usu) values (%s, %s)"
            val = (u.getnombre_usuario(), u.getcontrasena())
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Agregar Nuevo Usuario (DAO)!! ---", end="\n\n")
            system("pause")


# ----------------------------------------------------------------------

    def comprobarcodigoproducto(self, cantidad, texto):
        idproducto = ""
        while True:
            try:
                idproducto = input("Ingrese " + str(texto) + " : ")
                assert len(idproducto) >= 1 and len(idproducto) <= cantidad
            except AssertionError:
                print("Error en la cantidad de caracteres")
                system("pause")
            except:
                print("Error!")
                system("pause")
            else:
                break
        return idproducto

# ----------------------------------------------------------------------
    def comprobarcodigoventa(self, cantidad, texto):
        idventa = ""
        while True:
            try:
                idventa = input("Ingrese " + str(texto) + " : ")
                assert len(idventa) >= 1 and len(idventa) <= cantidad
            except AssertionError:
                print("Error en la cantidad de caracteres")
                system("pause")
            except:
                print("Error!")
                system("pause")
            else:
                break
        return idventa


# ---------------------------------------------------------------------


    def comprobarcodigodetalleventas(self, texto, cantidad):
        iddetalle = ""
        while True:
            try:
                idinforme = input("Ingrese " + str(texto) + " : ")
                assert len(iddetalle) >= 1 and len(iddetalle) <= cantidad
            except AssertionError:
                print("Error en la cantidad de caracteres")
                system("pause")
            except:
                print("Error!")
                system("pause")
            else:
                break
        return iddetalle

    def comprobarcodigoinformeventas(self, texto, cantidad):
        idinforme = ""
        while True:
            try:
                idinforme = input("Ingrese " + str(texto) + " : ")
                assert len(idinforme) >= 1 and len(idinforme) <= cantidad
            except AssertionError:
                print("Error en la cantidad de caracteres")
                system("pause")
            except:
                print("Error!")
                system("pause")
            else:
                break
        return idinforme


# ----------------------------------------------------------------------

    def agregarproducto(self, pro):
        try:
            codProdcuto = pro.getcodProducto()
            nombre = pro.getnombre()
            valorunitario = pro.getprecio_unitario()
            cantidad = pro.getcantidad()
            total = pro.gettotal()
            self.conectar()
            self.con.cursor()
            sql = "INSERT INTO Productos (Nombre,Codigo,Precio_Unitario,stock) values ( %s, %s, %s, %s)"
            val = (nombre, codProdcuto, valorunitario,  cantidad)
            self.cursor.execute(sql, val)
            id_producto = self.cursor.lastrowid  # Obtener el ID autoincremental
            self.con.commit()
            self.desconectar()
            print("\n--- Producto Agregado Correctamente!! ---\n")
            return id_producto  # Devuelve el ID del producto insertado
        except pymysql.Error as e:
            print(f"\n--- Error al agregar producto (DAO): {str(e)} ---\n")
        system("pause")

# ----------------------------------------------------------------------

# ----------------------------------------------------------------------

    def agregarventa(self, ven):
        try:
            # id  = ven.getidventa()
            fecha = ven.getfecha()
            tipo_documento = ven.gettipo_documento()
            id_vendedor = ven.getidvendedor()
            total_neto = ven.gettotal_neto()
            total_iva = ven.gettotal_iva()
            total_final = ven.gettotal_final()

            self.conectar()
            sql = "insert into Ventas (Fecha, Tipo_Documento, ID_Vendedor, Total_Neto, Total_IVA, Total_Final) values (%s, %s, %s, %s, %s, %s)"
            val = (fecha, tipo_documento, id_vendedor,
                   total_neto, total_iva, total_final)
            self.cursor.execute(sql, val)
            self.con.commit()

            sql = "SELECT LAST_INSERT_ID();"
            self.cursor.execute(sql)
            id_recien_generado = self.cursor.fetchone()
            self.desconectar()
            return id_recien_generado
        except pymysql.Error as e:
            print(f"\n--- Error al agregar venta (DAO): {str(e)} ---\n")
        system("pause")

# ----------------------------------------------------------------------


# ----------------------------------------------------------------------

    def agregarinformedeventas(self, i):
        try:
            # id = i.getidinforme()
            fecha = i.getfecha()
            cantidad_ventas_boletas = i.getcantidad_ventas_boletas()
            monto_boletas_netos = i.getmonto_boletas_neto()
            monto_boletas_iva = i.getmonto_boletas_iva()
            monto_boletas_total = i.getmonto_boletas_total()
            cantidad_facturas = i.getcantidad_facturas()
            monto_facturas_neto = i.getmonto_facturas_neto()
            monto_facturas_iva = i.getmonto_facturas_iva()
            monto_facturas_total = i.getmonto_facturas_total()
            id_vendedor = i.getid_vendedor()
            self.conectar()
            sql = "insert into Informe_Ventas (Fecha, Cantidad_Ventas_Boleta, Monto_Boletas_Neto, Monto_Boletas_IVA, Monto_Boletas_Total, Cantidad_Facturas, Monto_Facturas_Neto, Monto_Facturas_IVA, Monto_Facturas_Total, ID_Vendedor) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (fecha, cantidad_ventas_boletas, monto_boletas_netos, monto_boletas_iva, monto_boletas_total,
                   cantidad_facturas, monto_facturas_neto, monto_facturas_iva, monto_facturas_total, id_vendedor)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except pymysql.Error as e:
            print(
                f"\n--- Error al agregar informe de ventas (DAO): {str(e)} ---\n")
        system("pause")

# ----------------------------------------------------------------------

    def agregardetallesventas(self, det):
        try:

            # id = det.getid_detalle()
            id_venta = det.getid_venta()
            id_producto = det.getid_producto()
            cantidad = det.getcantidad()
            precio_unitario = det.getprecio_unitario()
            total = det.gettotal()

            self.conectar()
            sql = "insert into Detalles_Venta (ID_Venta, ID_Producto, Cantidad, Precio_Unitario, Total) values (%s, %s, %s, %s, %s)"
            val = (id_venta, id_producto, cantidad, precio_unitario, total)
            self.cursor.execute(sql, val)
            self.con.commit()

            sql = "SELECT LAST_INSERT_ID();"
            self.cursor.execute(sql)
            id_recien_generado = self.cursor.fetchone()
            self.desconectar()
            return id_recien_generado

        except pymysql.Error as e:
            print(
                f"\n--- Error al agregar detalles de ventas (DAO): {str(e)} ---\n")
        system("pause")


# ---------------------------------------------------------------------


    def agregarfactura(self, fac):
        try:

            # id = det.getid_detalle()
            # idfactura = fac.getidfactura()
            idventa = fac.getidventa()
            idcliente = fac.getidcliente()

            self.conectar()
            sql = "insert into Facturas (ID_Venta, ID_Cliente) values (%s, %s)"
            val = (idventa, idcliente)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except pymysql.Error as e:
            print(
                f"\n--- Error al agregar factura (DAO): {str(e)} ---\n")
        system("pause")


# ---------------------------------------------------------------------

    def obtenerproducto(self):
        try:
            self.conectar()
            sql = 'select * from productos;'
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except Exception:
            print("Error Al Obtener productos!!")
            system("pause")

# -----------------------------------------------------------------

    def obtenerventas(self):
        try:
            self.conectar()
            sql = 'select * from ventas;'
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except Exception:
            print("Error Al Obtener ventas!!")
            system("pause")

# -----------------------------------------------------------------


# -----------------------------------------------------------------

    def obtenerdetallesventas(self):
        try:
            self.conectar()
            sql = 'select * from detalles_ventas;'
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except Exception:
            print("Error Al Obtener ventas!!")
            system("pause")

# -----------------------------------------------------------------

    def obtenerinformedeventas(self):
        try:
            self.conectar()
            sql = 'select * from informe_ventas;'
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except Exception:
            print("Error Al Obtener ventas!!")
            system("pause")


# ----------------------------------------------------------------------

    def buscarproducto(self, pro):
        try:
            self.conectar()
            sql = 'select * from Productos where ID_Producto = %s;'
            val = (pro)
            self.cursor.execute(sql, val)
            rs = self.cursor.fetchone()
            self.desconectar()
            if rs is None:
                return False
            else:
                return True
        except pymysql.Error as e:
            print(
                f"\n--- Error al encontrar producto (DAO): {str(e)} ---\n")
        system("pause")


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

    def buscarventa(self, ven):
        try:
            self.conectar()
            sql = 'select * from Ventas where ID_Venta = %s;'
            val = (ven)
            self.cursor.execute(sql, val)
            rs = self.cursor.fetchone()
            self.desconectar()
            if rs is None:
                return False
            else:
                return True
        except pymysql.Error as e:
            print(
                f"\n--- Error al buscar id_venta (DAO): {str(e)} ---\n")
        system("pause")


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

    def buscardetatallesdeventas(self, iddetalle):
        try:
            self.conectar()
            sql = 'select * from Detalles_Venta where ID_Detalle = %s;'
            val = (iddetalle)
            self.cursor.execute(sql, val)
            rs = self.cursor.fetchone()
            self.desconectar()
            if rs is None:
                return False
            else:
                return True
        except pymysql.Error as e:
            print(
                f"\n--- Error al buscar id_detalle (DAO): {str(e)} ---\n")
        system("pause")


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

    def buscarinformedeventas(self, idinforme):
        try:
            self.conectar()
            sql = 'select * from informe_ventas where id_informe = %s;'
            val = (idinforme)
            self.cursor.execute(sql, val)
            rs = self.cursor.fetchone()
            self.desconectar()
            if rs is None:
                return False
            else:
                return True
        except pymysql.Error as e:
            print(
                f"\n--- Error al buscar id_informe (DAO): {str(e)} ---\n")
        system("pause")


# ----------------------------------------------------------------------


    def eliminarproducto(self, pro):
        try:
            self.conectar()
            sql = 'delete from Productos where id_producto = %s;'
            val = (pro)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except pymysql.Error as e:
            print(
                f"\n--- Error al eliminar producto (DAO): {str(e)} ---\n")
        system("pause")

# ----------------------------------------------------------------------
    def eliminarventa(self, ven):
        try:
            self.conectar()
            sql = 'delete from Ventas where ID_Venta = %s;'
            val = (ven)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except pymysql.Error as e:
            print(
                f"\n--- Error al eliminar venta (DAO): {str(e)} ---\n")
        system("pause")

    def eliminardetallesventas(self, ven):
        try:
            self.conectar()
            sql = 'delete from Detalles_Venta where Id_Detalle = %s;'
            val = (ven)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except pymysql.Error as e:
            print(
                f"\n--- Error al eliminar detalle (DAO): {str(e)} ---\n")
        system("pause")

# ----------------------------------------------------------------------
    def eliminarinformedeventas(self, ven):
        try:
            self.conectar()
            sql = 'delete from informe_ventas where id_informe = %s;'
            val = (ven)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except pymysql.Error as e:
            print(
                f"\n--- Error al eliminar informe (DAO): {str(e)} ---\n")
        system("pause")


# ----------------------------------------------------------------------

    def obtener_id_producto(self, nombre_producto):
        try:
            # Aquí realizas la consulta a la base de datos
            self.conectar()
            query = "SELECT id_producto FROM productos WHERE nombre = %s"
            # Ejecutas la consulta
            self.cursor.execute(query, (nombre_producto,))
            # Obtienes el resultado
            resultado = self.cursor.fetchone()  # Suponiendo que devuelve una sola fila
            self.desconectar()
            system("pause")
            if resultado:
                return resultado[0]  # Devuelve el id_producto encontrado
            else:
                return None  # Manejo si no se encuentra el producto
        except Exception as e:
            print(f"Error al obtener el id del producto: {e}")
            system("pause")
