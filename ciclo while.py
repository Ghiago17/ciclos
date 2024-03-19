def mostrar_menu():
    print("1. Personas")
    print("2. Vehiculos")
    print("3. Universidades")
    print("4. Notas")
    print("5. Salir")

def seleccionar_opcion():
    opcion = int(input("Por favor, selecciona una opción: "))
    if opcion == 1:
        print("Hola, has presionado la opción Personas")
    elif opcion == 2:
        print("Hola, has presionado la opción Vehiculos")
    elif opcion == 3:
        print("Hola, has presionado la opción Universidades")
    elif opcion == 4:
        print("Hola, has presionado la opción Notas")
    elif opcion == 5:
        print("Has presionado la opción Salir. El programa se cerrará.")
        return False
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
    return True

def main():
    continuar = True
    while continuar:
        mostrar_menu()
        continuar = seleccionar_opcion()

main()
