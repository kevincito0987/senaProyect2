def exercicio2():
    print(
            """
                Desarrollar un programa que permita almacenar las edades de un grupo de 10 personas en un vector de
                enteros y luego determine la cantidad de personas que son menores de edad, mayores de edad, cuántos
                adultos mayores, la edad más baja, la edad más alta y el promedio de edades ingresadas. Para el ejercicio
                anterior suponga que un adulto mayor debe tener una edad igual o superior a 60. Debe validar para cada
                ingreso que los valores estén en un rango entre 1 y 120 años. En caso de error deberá notificar y solicitar
                un nuevo valor. 
            """
        )
    
    while True:
        try:
            print("¿Cuántos personas desea almacenar?")
            cant = int(input())
            edades = []
            for i in range(cant):
                print("¿Cuál es la edad de la persona", i + 1, "?")
                edad = int(input())
                if edad < 1 or edad > 120:
                    print("La edad debe estar entre 1 y 120")
                    continue
                edades.append(edad)
            
            menores = 0
            mayores = 0
            adultos = 0
            promedio = 0
            menor = 30
            mayor = 0
            for edad in edades:
                if edad < 18:  # Ajustado para menores de 18
                    menores += 1
                elif edad >= 60:
                    mayores += 1
                if 18 <= edad <= 59:  # Rango para adultos
                    adultos += 1
                promedio += edad

                if edad < menor:
                    menor = edad
                if edad > mayor:
                    mayor = edad
            
            print("Cantidad de personas menores de 60:", menores)
            print("Cantidad de personas mayores de 60:", mayores)
            print("Cantidad de personas adultos:", adultos)
            print("Edad más baja:", menor)
            print("Edad más alta:", mayor)
            print("Promedio:", promedio / cant)
            break
        except ValueError:
            print("Ingresa un numero")