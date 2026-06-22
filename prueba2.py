#funciones
#Funcion para mostrar el menú principal
def mostrar_menu():
    print("********Menú Principal***********")
    print("1.- Agregar Reserva")
    print("2.- Buscar Reserva")
    print("3.- Eliminar Reserva")
    print("4.- Confirmar Reservas")
    print("5.- Mostrar Reservas")
    print("6.- Salir")
    print("*******************")
#Funcion que solicita la opcion del menu y la retorna
def seleccionar_opcion():
    while True:
        try:
            op = int(input("Seleccione una opción: "))
            if op <= 0 or op > 6:
                raise ValueError
            else:
                return op
        except ValueError:
            print("Debe ser un número entre el 1 y el 6")
#Opcion 1
#Funcion agregar reserva
def agregar_reserva(lista_r):
    nombre_completo = input("Ingrese el nombre completo: ")
    num_hab = input("Ingrese el número de habitación: ")
    cant_noches = input("Ingrese la cantidad de noches a hospedar: ")

#Funcion para validar el nombre
def validar_nombre(nombre):
    return nombre.strip().upper() != ""
#Funcion para validar número de habitación
def validar_habitacion(hab):
    
#Código Principal