def exercicio3():
    print(
            """
                Escriba un programa que lea dos vectores de números enteros ordenados ascendentemente y luego produzca la lista ordenada de la mezcla de los dos, por ejemplo, si los dos arreglos tienen los números 1 3 6 9 17 y 2 4 10 17, respectivamente, la lista de números en la pantalla debe ser 1 2 3 4 6 9 10 17 17. Limite los vectores a un tamaño de 5 y debe validar en cada ingreso que realmente se estén ingresando los datos de forma ascendente. 
            """
        )
    tamaño_maximo = input("¿Cuántos elementos desea almacenar en cada vector? ")
    tamaño_maximo = int(tamaño_maximo)
    procesar_vectores(tamaño_maximo)
    
    

def leer_vector_ordenado(tamaño):
    """
    Lee un vector de números enteros ordenados ascendentemente desde el usuario,
    validando que los datos se ingresen de forma ascendente.
    """
    vector = []
    for i in range(tamaño):
        while True:
            try:
                num = int(input(f"Ingrese el número {i+1} (debe ser mayor o igual al anterior): "))
                if i > 0 and num < vector[i-1]:
                    print("Error: El número debe ser mayor o igual al anterior.")
                else:
                    vector.append(num)
                    break
            except ValueError:
                print("Error: Ingrese un número entero válido.")
    return vector

def mezclar_vectores_ordenados(vector1, vector2):
    """
    Mezcla dos vectores ordenados ascendentemente en una nueva lista ordenada.
    """
    resultado = []
    i = j = 0
    while i < len(vector1) and j < len(vector2):
        if vector1[i] <= vector2[j]:
            resultado.append(vector1[i])
            i += 1
        else:
            resultado.append(vector2[j])
            j += 1
    # Agregar los elementos restantes de vector1 o vector2 (si los hay)
    resultado.extend(vector1[i:])
    resultado.extend(vector2[j:])
    return resultado

def procesar_vectores(tamaño_maximo):
    """
    Función principal que llama a las funciones para leer, validar y mezclar vectores.
    """
    # Leer los dos vectores
    print("Ingrese los datos del primer vector:")
    vector1 = leer_vector_ordenado(tamaño_maximo)
    print("\nIngrese los datos del segundo vector:")
    vector2 = leer_vector_ordenado(tamaño_maximo)

    # Mezclar los vectores y mostrar el resultado
    vector_mezclado = mezclar_vectores_ordenados(vector1, vector2)
    print("\nLa lista ordenada de la mezcla es:")
    print(*vector_mezclado)