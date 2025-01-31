from math import pi

def exercicio1():
    print(
            """
                Desarrollar un programa que permita calcular el área o perímetro de algunas figuras planas según sea un triángulo, rectángulo, cuadrado o círculo.
                """
        )
    
    while True:
        try:
            print("¿Qué figura planes desea calcular? (t/r/c/o): ")
            opc = input()
            try:
                match opc:
                    case 'o':
                        print("¿Cuál es el radio del círculo? ")
                        radio = float(input())
                        print("¿Cuál es el alto de la figura? ")
                        alto = float(input())
                        print("El área de la figura es:", pi * (radio ** 2))
                        print("El perímetro de la figura es:", 2 *  pi * (radio ** 2))
                        break
                    case 'r':
                        print("¿Cuál es el ancho de la figura?")
                        ancho = float(input())
                        print("¿Cuál es el alto de la figura?")
                        alto = float(input())
                        print("El área de la figura es:", ancho * alto)
                        print("El perímetro de la figura es:", 2 * (ancho + alto))
                        break
                    case 't':
                        print("¿Cuál es la altura del triángulo?")
                        altura = float(input())
                        print("¿Cuanto mide el lado 1 del triángulo?")
                        l1 = float(input())
                        print("¿Cuanto mide el lado 2 del triángulo?")
                        l2 = float(input())
                        print("¿Cuanto mide el lado 3 del triángulo?")
                        l3 = float(input())
                        print("El área de la figura es:", l1 * altura / 2)
                        print("El perímetro de la figura es:", l1 + l2 + l3)
                        break
                    case 'c':
                        print("¿Cuanto mide el lado 1 del triángulo?")
                        l1 = float(input())
                        print("¿Cuanto mide el lado 2 del triángulo?")
                        l2 = float(input())
                        print("El área de la figura es:", l1 * l2)
                        print("El perímetro de la figura es:", 2 * (l1 + l2))
                        break
                    case _ : print("Opción no valida")
            except ValueError:
                print("Ingresa un numero")
        except ValueError:
            print("Ingresa un numero")