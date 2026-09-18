


nombres = []
telefonos = []
emails = []
direcciones = []

contactos= {}

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
        contactos[nombre] = {
            "Email": email,
            "telefono" : telefono,
            "direccion" : direccion
        }
        print(f"Contacto {nombre} guardado exitosamente")
    elif opcion_elegida == 2:
        nombre = input("Ingrese el nombre a buscar: ")
        if nombre in contactos:
            print("="*10)
            print(contactos[nombre])
            print("="*10)
        else:
             print("Contacto no existe")
    elif opcion_elegida == 3:
        pass
    elif opcion_elegida == 4:
            for nombre,telefono,email,direccion in zip(nombres,telefonos,emails,direcciones):
                print(f"Nombre: {nombre}")
                print(f"Telefono: {telefono}")
                print(f"Email: {email}")
                print(f"Direccion: {direccion}")
                print("="*10)
    elif opcion_elegida == 5:
        print("Hasta la vida Baby")
        break
    else:
        print("Opcion invalida, intenta nuevamente")