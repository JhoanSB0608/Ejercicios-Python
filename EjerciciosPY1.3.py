def calcular_area():
    opcion = input("¿Qué figura quiere calcular? (Escriba T o C): ")

    if opcion == "T":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = base * altura / 2
        print("El área del triángulo es:", area)
    
    elif opcion == "C":
        radio = float(input("Ingrese el radio del círculo: "))
        area = 3.141592 * radio * radio
        print("El área del círculo es:", area)
    
    else:
        print("Opción no válida. Por favor, ingrese T o C.")

calcular_area()