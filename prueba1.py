def mostrar_menu():
    print("**************************************************")
    print("|| 1.- agregar mascota       ||")
    print("|| 2.- buscar mascota        ||")
    print("|| 3.- eliminar mascota      ||")
    print("|| 4.- macrcar como vacunada     ||")
    print("|| 5.- mostrar mascotas      ||")
    print("|| 6.- salir     ||")
    print("**************************************************")


def validar_nombre(name):
    return name.strip() != ""

def validar_especie(especie):
    especies_validas = ["perro", "gato", "ave"]
    return especie.strip().lower() in especies_validas

def validar_edad(edad):
    return edad.isdigit() and int(edad) > 0

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
 
def  agregar_mascota(lista_m):
    
    nombre = input("ingrese el nombre de su mascota:    ")
    correcta = validar_nombre(nombre)
    
    if not correcta:
        print("el nombre no puede estar en blanco")
        return
    especie = input("ingrese la especie (perro,gato o ave)")
    correcta = validar_especie(especie)
    
    if not correcta:
        print("la especie solo puede ser perro, gato o ave")
        return
    edad = input("ingrese la edad de la mascota:    ")
    correcta = validar_edad(edad)
    
    if not correcta:
        print("la edad debe ser numeros enteros mayor a cero")
        return
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip(),
        "edad": int(edad),
        "vacunada": False
    }
    lista_m.append(mascota)
    print("mostrar agregada correctamente")


datos_mascotas = []
op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opcion()

    if op == 1:
        agregar_mascota(datos_mascotas)
    if op == 2:
        print()
    if op == 3:
        print()
    if op == 4:
        print()
    if op == 5:
        print()
    if op == 6:
        print()
        print("GRACIAS POR USAR EL SISTEMA. VUELVA PRONTO")
