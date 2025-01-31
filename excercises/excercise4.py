def excercise4():
        print(
                """
                        Una emisora con presencia en diferentes ciudades desea conocer el rating de canciones y cantantes más escuchados (sonados) en este semestre del año. Por lo tanto, se ha pedido a estudiantes del SENA del programa de tecnólogo en análisis y desarrollo de software desarrollar una solución que permita conocer la respuesta de 6 personas con relación a sus gustos musicales. Con fines administrativos y realizar una rifa entre las personas encuestadas, la emisora desea poder registrar de las personas entrevistadas su nombre, número de identificación (cédula), fecha de nacimiento, correo electrónico, ciudad de residencia, ciudad de origen. Además, se deberá poder almacenar el artista y título de hasta 3 canciones favoritas en  GFPI-F-135 V01 cada una de las personas que se ingrese, teniendo en cuenta lo anterior, se sugiere que la solución deberá mostrar un menú que permite las siguientes opciones:
                            a. Agregar una persona con los datos que se listan anteriormente.
                            b. Mostrar la información personal de una persona particular por medio de su posición en el vector. 
                """
            )

        print("\n--- Menú ---")
        print("a. Agregar una persona")
        print("b. Mostrar información de una persona")
        print("s. Salir")

        personas = []
        while True:
                opcion = input("Seleccione una opción: ").lower()

                if opcion == "a":
                        agregar_persona(personas)
                elif opcion == "b":
                        mostrar_informacion_persona(personas)
                elif opcion == "s":
                        break
                else:
                        print("Opción inválida. Intente de nuevo.")

            

def agregar_persona(personas):
    """
    Agrega una persona con sus datos y canciones favoritas a la lista.
    """
    nombre = input("Ingrese el nombre: ")
    cedula = input("Ingrese el número de identificación (cédula): ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
    correo = input("Ingrese el correo electrónico: ")
    ciudad_residencia = input("Ingrese la ciudad de residencia: ")
    ciudad_origen = input("Ingrese la ciudad de origen: ")

    canciones = []
    for i in range(3):
        artista = input(f"Ingrese el artista de la canción {i+1} (o deje en blanco si no tiene): ")
        if artista:  # Si se ingresó un artista, pedir la canción
            titulo = input(f"Ingrese el título de la canción {i+1}: ")
            canciones.append({"artista": artista, "titulo": titulo})
        else:  # Si no se ingresó artista, no se pide la canción
            break

    persona = {
        "nombre": nombre,
        "cedula": cedula,
        "fecha_nacimiento": fecha_nacimiento,
        "correo": correo,
        "ciudad_residencia": ciudad_residencia,
        "ciudad_origen": ciudad_origen,
        "canciones": canciones,
    }
    personas.append(persona)
    print("¡Persona agregada exitosamente!")

def mostrar_informacion_persona(personas):
    """
    Muestra la información personal y canciones favoritas de una persona.
    """
    if not personas:
        print("No hay personas registradas.")
        return

    while True:
        try:
            posicion = int(input("Ingrese la posición de la persona (1 a {}): ".format(len(personas))))
            if 1 <= posicion <= len(personas):
                break
            else:
                print("Error: La posición debe estar entre 1 y {}.".format(len(personas)))
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    persona = personas[posicion - 1]
    print("\n--- Información de la persona ---")
    for clave, valor in persona.items():
        if clave == "canciones":
            print("Canciones favoritas:")
            for cancion in valor:
                print(f"- {cancion['titulo']} de {cancion['artista']}")
        else:
            print(f"{clave.capitalize()}: {valor}")
