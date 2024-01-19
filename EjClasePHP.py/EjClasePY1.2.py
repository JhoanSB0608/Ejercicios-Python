def ingresar_resultados():
    equipo1 = input("Ingrese el nombre del equipo 1: ")
    equipo2 = input("Ingrese el nombre del equipo 2: ")

    canastas_equipo1 = int(input(f"Ingrese el total de canastas para {equipo1}: "))
    canastas_equipo2 = int(input(f"Ingrese el total de canastas para {equipo2}: "))

    return equipo1, canastas_equipo1, equipo2, canastas_equipo2


def mostrar_informacion(equipo_ganador, equipo_perdedor, diferencia_canastas):
    print("\nInformación del partido:")
    print(f"Equipo ganador: {equipo_ganador}")
    print(f"Equipo perdedor: {equipo_perdedor}")
    print(f"Diferencia de canastas: {diferencia_canastas}")


def main():
    equipo1, canastas_equipo1, equipo2, canastas_equipo2 = ingresar_resultados()

    if canastas_equipo1 > canastas_equipo2:
        equipo_ganador = equipo1
        equipo_perdedor = equipo2
        diferencia_canastas = canastas_equipo1 - canastas_equipo2
    elif canastas_equipo2 > canastas_equipo1:
        equipo_ganador = equipo2
        equipo_perdedor = equipo1
        diferencia_canastas = canastas_equipo2 - canastas_equipo1
    else:
        print("¡Empate! Ambos equipos tienen la misma cantidad de canastas.")
        return

    mostrar_informacion(equipo_ganador, equipo_perdedor, diferencia_canastas)


if __name__ == "__main__":
    main()