def mostrar_menu():
    print("**************************************************")
    print("|| 1.- agregar mascota       ||")
    print("|| 2.- buscar mascota        ||")
    print("|| 3.- eliminar mascota      ||")
    print("|| 4.- macrcar como vacunada     ||")
    print("|| 5.- mostrar mascotas      ||")
    print("|| 6.- salir     ||")
    print("**************************************************")

def solicitar_opcion():
    while True:
        try:
            opcion = int(input("debe ingresar una opcion:   "))
            if opcion < 1 or opcion > 6:
                print("debe seleccionar una opcion del 1 al 6")
            else:
                break
        except ValueError:
            print("debe ingresar un numero entero")
    return opcion       




datos_mascotas = []
op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opcion()