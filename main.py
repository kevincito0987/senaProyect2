from excercises.excercise1 import exercicio1

while True:
    try:
        print(
            """
                Bienvenido al sistema de Ejercicios del SENA :):)
                Selecciona:
                1.Ejercico 1
                2.Ejercico 2
                3.Ejercico 3
                4.Ejercico 4
                0.Salir
                """
        )
        opc = int(input())
        try:
            while True:
                match opc:
                    case 1:
                        exercicio1()
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break
                    case 2:
                        print("Ejercicio 2")
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break
                    case 3:
                        print("Ejercicio 3")
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break
                    case 4:
                        print("Ejercicio 4")
                        continuar = input("¿Desea continuar? (s/n): ")
                        if continuar.lower() != 's':
                            break
                    case 0 : break
                    case _ : print("Opcion no valida")
        except ValueError:
            print("Ingresa un numero porfa.")
    except ValueError:
        print("Ingresa un numero")
