#Funciones
#opcion 2: Buscar mascota
def buscar_mascota(lista_m, nombre_m):
    #recorrer y devolver la posicion
    for i in range(len(lista_m)):
        if lista_m[i]["nombre"] == nombre_m:
            return i #retorno la posición
    return -1 #se termino el ciclo por tanto no se encontró


def mostrar_menu():
    print("===========================")
    print("|| 1.- Agregar Mascota     ||")
    print("|| 2.- Buscar Mascota     ||")
    print("|| 3.- Eliminar Mascota     ||")
    print("|| 4.- Marcar como Vacunada ||")
    print("|| 5.- Mostrar Mascotas     ||")
    print("|| 6.- Salir              ||")
    print("===========================")

#funciones de validaciones
def validar_nombre(name):
    #strip() -> eliminar todos los espacios en blanco al inicio y al final de un string
    #Retorna True si es válido o False si no
    return name.strip() != ""

def validar_especie(especie):
    especies_validas = ["perro", "gato", "ave"]
    #retorna True si lo consigue o False si no
    return especie.strip().lower() in especies_validas

def validar_edad(edad):
    #isdigit() -> revisa si un string contiene solo digitos
    return edad.isdigit() and int(edad) > 0


def solicitar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion < 1 or opcion > 6:
                print("Debe seleccionar una opción del 1 al 6")
            else:
                break
        except ValueError:
            print("Debe ingresar un número")
    return opcion

#Funcion para la opción 1
def agregar_mascota(lista_m):
    #solicitamos los datos
    nombre = input("Ingrese el nombre de su mascota: ")
    correcta = validar_nombre(nombre)
    if not correcta:
        print("El nombre no puede estar en blanco")
        return
    especie = input("Ingrese la especie (perro,gato o ave)")
    correcta = validar_especie(especie)
    if not correcta:
        print("La especie solo puede ser perro, gato o ave")
        return
    edad = input("Ingrese la edad de la mascota: ")
    correcta = validar_edad(edad)
    if not correcta:
        print("La edad debe ser un número entero mayor a cero")
        return
    #agregar los datos al diccionario
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip().lower(),
        "edad": int(edad),
        "vacunada": False
    }
    #agrego a la lista
    lista_m.append(mascota)
    print("Mascota agregada correctamente")

#opcion 4
def actualizar_vacunas(lista_m):
    #recorre la lista completa
    for m in lista_m:
        #preguntamos por la edad para validar
        if m["edad"] >= 1:
            m["vacunada"] = True
        else:
            m["vacunada"] = False
#Código Principal
#declarar la lista de mascotas
datos_mascotas = []
op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opcion()

    if op == 1:
        agregar_mascota(datos_mascotas)
    elif op == 2:
        print("**** Buscar Mascota *****")
        #solicitar el nombre de la mascota a buscar
        nom = input("Ingrese el nombre d ela mascota a buscar: ")
        posicion = buscar_mascota(datos_mascotas, nom)
        if posicion != -1:
            #guardar en una variable el diccionario de la mascota en la posicion de la lista
            m = datos_mascotas[posicion]
            print(f"Mascota encontrada en la posición: {posicion}")
            print(f"Nombre Mascota: {m['nombre']}")
            print(f"Especie Mascota: {m['especie']}")
            print(f"Edad Mascota: {m['edad']}")
            print(f"Vacunada: {m['vacunada']}")
        else:
            print(f"No se encontró la mascota con el  nombre: {nom}")

    elif op == 3:
        print("**** Eliminar Mascota *****")
        #solicitar el nombre de la mascota a buscar
        nom = input("Ingrese el nombre de la mascota a eliminar: ")
        posicion = buscar_mascota(datos_mascotas, nom)
        if posicion != -1:
            #procedemos a eliminarla
            datos_mascotas.pop(posicion)
            print("Mascota eliminada correctamente")
        else:
            print(f"La mascota '{nom}' no se encuentra registrada")

    elif op == 4:
        actualizar_vacunas(datos_mascotas)
        print("Estado de vacunas actualizadas")
    elif op == 5:
        #actualizar el estado de las vacunas
        actualizar_vacunas(datos_mascotas)
        #mostrar sus datos
        #si la lista esta vacia
        if len(datos_mascotas) == 0:
            print("No hay mascotas en la lista")
        else:
            print("== Lista de Mascotas ==")
            for m in datos_mascotas:
                print(f"Nombre: {m['nombre']}")
                print(f"Especie: {m['especie']}")
                print(f"Edad: {m['edad']}")
                #variable pra cambiar el valor de vacunada
                estado = "AL DÍA" if m["vacunada"] else "PENDIENTE"
                print(f"Estado Vacuna: {estado}")
    elif op == 6:
        print("Gracias por usar el sistema. Vuelva pronto")