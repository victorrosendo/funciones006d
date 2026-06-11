#Funciones
def mostrar_encabezado():
    print("=====================")
    print("|| Sistema de Registro Escolar ||")
    print("=====================")

def datos_estudiantes():
    estudiante = {}
    estudiante["nombre"] = input("Ingrese el nombre del estudiante: ")
    while True:
        try:
            estudiante["semestre"] = int(input("Ingrese el semestre que cursa: "))
            if estudiante["semestre"] < 1 or estudiante["semestre"] > 5:
                print("Debe ingresar un semestre del 1 al 5")
            else:
                break
        except ValueError:
            print("Debe ingresar números")
    estudiante["carrera"] = input("Ingrese la carrera que estudia: ")
    estudiante["rut"] = input("Ingrese el rut del estudiante: ")
    return estudiante
    #estudiante["nombre"] = nombre
    #estudiante["semestre"] = semestre
    #estudiante["carrera"] = carrera
    #estudiante["rut"] = rut
    """
    estudiante = {
        "carrera" : carrera,
        "rut": rut,
        "nombre": nombre
    }
    """

def mostrar_ficha(estudiante):
    print(f"Nombre Estudiante: {estudiante["nombre"]}")
    print(f"Rut Estudiante: {estudiante["rut"]}")
    print(f"Carrera Estudiante: {estudiante["carrera"]}")
    print(f"Semestre Estudiante: {estudiante["semestre"]}")


#Código Principal
datos = datos_estudiantes()
mostrar_encabezado()
mostrar_ficha(datos)