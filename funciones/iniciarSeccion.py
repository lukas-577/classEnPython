from os import system
import getpass
from classes.usuario import usuario
# Asegúrate de importar correctamente tu función menu
from funciones.menu import menu
# Importa menuInicial para manejar el error de inicio de sesión
from funciones.menuInicial import menuInicial
from DAO import DAO

# instancia global de usuario
sesion = usuario()


def iniciar_sesion():

    instancia_dao = DAO()

    while True:
        try:
            system("cls")
            print("--- LOGIN ---")
            nombre_usuario = input("Digite El Nombre de Usuario: ")

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
                f"Digite La Contraseña Del Usuario ({nombre_usuario.upper()}): ")
            if len(contrasena) < 1 or len(contrasena) > 50:
                print("\n--- Debe Tener Entre 1 y 50 Caracteres!! ---")
                system("pause")
            else:
                break
        except Exception as e:
            print(f"\n--- Error Al Ingresar Contraseña (Login): {e} ---")
            system("pause")

    system("cls")

    r = instancia_dao.iniciarSesion(nombre_usuario, contrasena)
    if r is None:
        print("\n--- Error de Usuario y/o Contraseña!! ---\n")
        system("pause")
        menuInicial()
    else:
        sesion.setid_usuario(r[0])
        sesion.setnombre_usuario(r[1])
        sesion.setcontrasena(r[2])
        sesion.settipo_usuario(r[3])
        print(
            f"\n--- Bienvenido Usuario {sesion.getnombre_usuario().upper()} !! ---\n")
        system("pause")
        menu()
