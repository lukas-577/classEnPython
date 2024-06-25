from os import system
from DAO import DAO
from classes.usuario import usuario


class MenuInicial:

    d = DAO()
    sesion = usuario()

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
                    self.__iniciarsesion()
                elif op == 2:
                    self.__crearCuenta()
                elif op == 3:
                    self.__salir()
                    break
            except:
                print("Error Al Digitar Opcion")
                system("pause")
