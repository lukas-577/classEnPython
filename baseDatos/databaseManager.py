import pymysql


class DatabaseManager:
    def __init__(self):
        self.con = None
        self.cursor = None

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

    def desconectar(self):
        if self.con:
            self.con.close()
            print("Desconexión exitosa de MySQL")
