longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))
def calcular_area_rectangulo(longitud, ancho):
    if longitud > 0 and ancho > 0:
        area = longitud * ancho
        print("El área del rectángulo es:", area)
    else:
        print("Error: Los lados deben ser positivos.")

calcular_area_rectangulo(longitud, ancho)
