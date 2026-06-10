#Funciones
def datos_producto(name, stock, price): #no importa el orden de los parametros
    print("===================")
    print(f"||Nombre del producto {name} ||")
    print(f"||Precio del producto {price} ||")
    print(f"||Stock del producto {stock} ||")
    print("===================")


#Código Principal
nombre = input("Ingrese el nombre del producto: ")
while True:
    try:
        precio = int(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("Debe ser un número positivo")
        else:
            break
    except ValueError:
        print("Debe escribir números")
while True:
    try:
        stock = int(input("Ingrese el stock del producto: "))
        if stock < 0:
            print("Debe ser un número positivo")
        else:
            break
    except ValueError:
        print("Debe escribir números")

#llamar a la funcion
datos_producto(nombre,stock,precio)#se deben enviar los parametros en el orden exacto que los declare al crear la funcion