from os import system
from funciones.iniciarSeccion import IniciarSesion


class MenuInicial:

    def __init__(self):
        pass

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
                    i = IniciarSesion()
                    i.iniciarsesion()
                elif op == 2:
                    self.__crearCuenta()
                elif op == 3:
                    self.__salir()
                    break
            except:
                print("Error Al Digitar Opcion")
                #     system("pause")
