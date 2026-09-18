


nombres = []
telefonos = []
emails = []
direcciones = []

contactos = {}
while True:
    menu = """

    ### ELIGE UNA OPCION ###
    1. Agregar un contacto
    2. Buscar un contacto
    3. Eliminar un contacto
    4. Ver contacto
    5. Salir
    """

    opcion_elegida = int(input(menu))

    if opcion_elegida == 1:
        nombre = input("Ingrese el nombre: ")
        nombre = nombre.lower()
        telefono = input("Ingrese el telefono: ")
        email = input("Ingrese el email: ")
        direccion = input("Ingrese la direccion: ")
        nombres.append(nombre)
        telefonos.append(telefono)
        emails.append(email)
        direcciones.append(direccion)
        print(f"Contacto {nombre} guardado exitosamente")
    elif opcion_elegida == 2:
        nombre = input("Ingrese el nombre a buscar: ")
        if nombre in nombres:
             indice = nombres.index(nombre.lower())
             print(f"Nombre: {nombre[indice]}")
             print(f"Telefono: {telefono[indice]}")
             print(f"Email: {email[indice]}")
             print(f"Direccion: {direccion[indice]}")
             print("="*10)
        else:
             print("Contacto no existe")
    elif opcion_elegida == 3:
        nombre = input("Ingrese el contacto a eliminar: ")
        if nombre in contactos:
            del contactos[nombre]
            print(f"Contacto {nombre} eliminado exitosamente")
        else:
            print(f"Contacto {nombre} no existe")
    elif opcion_elegida == 4:
            for i, key in enumerate(contactos):
                 print(i+1, "-,key")
                
    elif opcion_elegida == 5:
        print("Hasta la vida Baby")
        break
    else:
        print("Opcion invalida, intenta nuevamente")