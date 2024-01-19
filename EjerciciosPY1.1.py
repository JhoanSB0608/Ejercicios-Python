numero = int(input("Ingrese un número: "))
def determinar_positivo_menor_100(numero):
    if numero > 0 and numero < 100:
        print("El número es positivo y menor que 100.")
    else:
        print("El número no cumple con la condición especificada.")

determinar_positivo_menor_100(numero)