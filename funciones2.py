#Funciones
def convertir_calificacion(puntaje, puntaje_total):
    nota = (puntaje * 6 / puntaje_total) + 1
    return round(nota, 1)


#Código Principal
while True:
    try:
        p = float(input("Ingrese el puntaje del estudiante: "))
        if p < 0:
            print("Ingrese un valor válido")
        else:
            break
    except ValueError:
        print("Debe ingresar solo números")

while True:
    try:
        pt = float(input("Ingrese el puntaje total de la evaluación: "))
        if pt < 0:
            print("Ingrese un valor válido")
        else:
            break
    except ValueError:
        print("Debe ingresar solo números")
#llamar a la funcion
calif = convertir_calificacion(p,pt)
print(f"La calificación en escala chilena es: {calif}")
