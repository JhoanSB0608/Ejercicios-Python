def analizar_numeros():
    numeros_pares = 0
    numeros_impares = 0
    total_numeros = 0
    sumatoria_total = 0
    mayores_50 = 0
    entre_20_y_50 = 0
    menores_10 = 0

    while True:
        numero = int(input("Ingrese un número (ingrese un número negativo para finalizar): "))
        
        if numero < 0:
            break

        total_numeros += 1
        sumatoria_total += numero

        if numero % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1

        if numero > 50:
            mayores_50 += 1
        elif 20 < numero <= 50:
            entre_20_y_50 += 1
        elif numero < 10:
            menores_10 += 1

    if total_numeros > 0:
        promedio_numeros = sumatoria_total / total_numeros
        print("\nResultados:")
        print(f"Total de números pares: {numeros_pares}")
        print(f"Total de números impares: {numeros_impares}")
        print(f"Promedio de los números ingresados: {promedio_numeros}")
        print(f"Sumatoria total de los números ingresados: {sumatoria_total}")
        print(f"Total de números mayores de 50: {mayores_50}")
        print(f"Total de números mayores de 20 y menores de 50: {entre_20_y_50}")
        print(f"Total de números menores de 10: {menores_10}")
    else:
        print("No se ingresaron números.")

analizar_numeros()