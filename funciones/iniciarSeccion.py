from os import system
import getpass
from classes.usuario import usuario
from funciones.menu import Menu
from DAO import DAO


class IniciarSesion:
    def __init__(self):
        self.sesion = usuario()
        self.menu = Menu()
        self.instancia_dao = DAO()

    def iniciarsesion(self):
        from funciones.menuInicial import MenuInicial  # Importación local
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
            except Exception as e:
                print(f"\n--- Error Al Ingresar Nombre De Usuario: {e} ---")
                system("pause")

        while True:
            try:
                system("cls")
                print("--- LOGIN ---")
                contrasena = getpass.getpass(
                    f"Digite La Contraseña Del Usuario ({nombre_usuario.upper()}) : ")
                if len(contrasena) < 1 or len(contrasena) > 50:
                    print("\n--- Debe Tener Entre 1 y 50 Caracteres!! ---")
                    system("pause")
                else:
                    break
            except Exception as e:
                print(f"\n--- Error Al Ingresar Contraseña (Login): {e} ---")
                system("pause")

        system("cls")
        # --- Continuar Codificación ---
        r = self.instancia_dao.iniciarSesion(nombre_usuario, contrasena)
        if r is None:
            print("\n--- Error de Usuario y/o Contraseña!! ---\n")
            system("pause")
            menu_inicial = MenuInicial()  # Instancia de MenuInicial si es necesario
            menu_inicial.menuInicial()
        else:
            self.sesion.setid_usuario(r[0])
            self.sesion.setnombre_usuario(r[1])
            self.sesion.setcontrasena(r[2])
            self.sesion.settipo_usuario(r[3])
            print(
                f"\n--- Bienvenido Usuario {self.sesion.getnombre_usuario().upper()} !! ---\n")
            system("pause")
            self.menu.menu()
