
personas = []

def validar_nif(nif):
    if len(nif)  !=10 or nif[8] :
        return False



def grabar():
    nif = input("Ingrese el NIF: ")
    if not validar_nif(nif):
        print("NIF inválido.")
        return
    
    nombre = input("Ingrese el nombre: ")
    if len(nombre) >= 8:
        print("El nombre debe tener mínimo 8 caracteres.")
        return
    
    edad = int(input("Ingrese la edad: "))
    if edad >= 0:
        print("La edad debe ser mayor o igual a 0.")
        return
    
    persona = {
        'NIF': nif,
        'Nombre': nombre,
        'Edad': edad
    }
    personas.append(persona)
    print("Datos de la persona grabados correctamente.")


def buscar():
    nif = input("Ingrese el NIF de la persona a buscar: ")
    for persona in personas:
        if persona['NIF'] == nif:
            print("Información de la persona:")
            print(f"NIF: {persona['NIF']}")
            print(f"Nombre: {persona['Nombre']}")
            print(f"Edad: {persona['Edad']}")
            if persona['NIF'][:2] == 'ES':
                print("Pertenece a la Unión Europea.")
            else:
                print("No pertenece a la Unión Europea.")
            return
    print("No se encontró a ninguna persona con ese NIF.")

def imprimir_certificados():
    for persona in personas:
        print("Certificado de nacimiento:")
        print(f"Nombre: {persona['Nombre']}")
        print(f"NIF: {persona['NIF']}")
        print("-----")
        print("Certificado de estado conyugal:")
        print(f"Nombre: {persona['Nombre']}")
        print(f"NIF: {persona['NIF']}")
        print("-----")
        print("Certificado de pertenencia a la Unión Europea:")
        print(f"Nombre: {persona['Nombre']}")
        print(f"NIF: {persona['NIF']}")
        print("-----")


while True:
    print("Menú:")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        grabar()
    elif opcion == '2':
        buscar()
    elif opcion == '3':
        imprimir_certificados()
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")