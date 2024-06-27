from os import system


def menuInicial():
    from funciones.iniciarSeccion import iniciar_sesion
    while True:
        try:
            system("cls")
            print("MENU ")
            print("1.Iniciar Sesion")
            print("2.Registrarse")
            print("3.Salir")
            op = int(input("Digite Una opcion : "))
            if op == 1:
                iniciar_sesion()
            # elif op == 2:
            #     self.__crearCuenta()
            # elif op == 3:
            #     self.__salir()
            #     break
        except Exception as e:
            print("Error: ", e)
            system("pause")
