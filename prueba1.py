def buscar_mascota(lista_m, nombre_m):
    for i in range(len(lista_m)):
        if lista_m[i]["nombre"] == nombre_m:
            return i 
    return -1

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
    especie = input("ingrese la especie (perro,gato o ave): ")
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
def actualizar_vacunas(lista_m):
    for m in lista_m:
        if m["edad"] >=1:
            m["vacunada"] = True
        else:
            m["vacunada"] = False

datos_mascotas = []
op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opcion()

    if op == 1:
        agregar_mascota(datos_mascotas)
    elif op == 2:
        print("***** BUSCAR MASCOTA *****")
        nom = input("ingrese el nombre de la mascota a buscar:  ")
        posicion = buscar_mascota(datos_mascotas, nom)
        if posicion != -1:
            m = datos_mascotas[posicion]
            print(f"mascota encontrada en la posicion: {posicion}")
            print(f"nombre mascota: {m['nombre']}")
            print(f"especie mascota: {m['especie']}")
            print(f"edad mascota: {m['edad']}")
            print(f"vacunada: {m['vacunada']}")
        else:
            print(f"no se logro encontrar la mascota con el nombre: {nom}")
    elif op == 3:
        print("***** ELIMINAR MASCOTA *****")
        nom = input("ingrese el nombre de la mascota a eliminar:    ")
        posicion = buscar_mascota(datos_mascotas, nom)
        if posicion != -1:
            datos_mascotas.pop(posicion)
            print("mascota eliminada correctamente")
        else:
            print(f"la mascota '{nom}' no se encuentra registrada")

    elif op == 4:
        actualizar_vacunas(datos_mascotas)
        print("estado de vacunas actualizadas")
    elif op == 5:
        actualizar_vacunas(datos_mascotas)
        if len (datos_mascotas) == 0:
            print("no hay ,mascotas en la lista")
        else:
            print("== lista de mascotas ==")
            for m in datos_mascotas:
                print(f"nombre mascota: {m['nombre']}")
                print(f"especie mascota: {m['especie']}")
                print(f"edad mascota: {m['edad']}")
                estado = "AL DIA" if m["vacunada"] else "pendiente"
                print(f"estado vacuna: {estado}")
    elif op == 6:
        print()
        print("GRACIAS POR USAR EL SISTEMA. VUELVA PRONTO")
