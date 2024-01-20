titulo = """
    ++++++++++++++++++++++++++++++++++++++++++
    +   Proyecto Liga Colombiana De Futbol   +
    ++++++++++++++++++++++++++++++++++++++++++
"""
class Torneo:
    def __init__(self):
        self.equipos = []

    def agregar_equipo(self):
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        equipo = [nombre_equipo, 0, 0, 0, 0, 0, 0, 0]  # [Nombre, PJ, PG, PE, PP, GF, GC, TP]
        self.equipos.append(equipo)
        print(f"Equipo {nombre_equipo} registrado con éxito.")

    def registrar_fecha_partido(self):
        fecha = input("Ingrese la fecha: ")
        local = input("Ingrese el nombre del equipo local: ")
        visitante = input("Ingrese el nombre del equipo visitante: ")
        goles_local = int(input(f"Ingrese los goles anotados por {local}: "))
        goles_visitante = int(input(f"Ingrese los goles anotados por {visitante}: "))
        self.actualizar_tabla(local, visitante, goles_local, goles_visitante)
        print(f"Fecha {fecha} registrada con éxito.")

    def actualizar_tabla(self, local, visitante, goles_local, goles_visitante):
        equipo_local = next(equipo for equipo in self.equipos if equipo[0] == local)
        equipo_visitante = next(equipo for equipo in self.equipos if equipo[0] == visitante)

        equipo_local[1] += 1  # PJ
        equipo_visitante[1] += 1  # PJ
        if goles_local > goles_visitante:
            equipo_local[2] += 1  # PG
            equipo_local[7] += 3  # TP
            equipo_visitante[4] += 1  # PP
        elif goles_local < goles_visitante:
            equipo_visitante[2] += 1  # PG
            equipo_visitante[7] += 3  # TP
            equipo_local[4] += 1  # PP
        else:
            equipo_local[3] += 1  # PE
            equipo_local[7] += 1  # TP
            equipo_visitante[3] += 1  # PE
            equipo_visitante[7] += 1  # TP

        equipo_local[5] += goles_local  # GF
        equipo_local[6] += goles_visitante  # GC

        equipo_visitante[5] += goles_visitante  # GF
        equipo_visitante[6] += goles_local  # GC

    def mostrar_tabla_posiciones(self):
        # Ordenar la lista de equipos por el total de puntos (equipo[7]) de manera descendente
        equipos_ordenados = sorted(self.equipos, key=lambda x: x[7], reverse=True)

        print("\nTabla de Posiciones:")
        print("----------------------------------------------------------------")
        print("Equipo\t\tPJ\tPG\tPE\tPP\tGF\tGC\tTP")
        print("----------------------------------------------------------------")
        for equipo in equipos_ordenados:
            print("----------------------------------------------------------------")
            print(f"{equipo[0]}\t{equipo[1]}\t{equipo[2]}\t{equipo[3]}\t{equipo[4]}\t{equipo[5]}\t{equipo[6]}\t{equipo[7]}")

    def reportes(self):
        equipo_max_goles = max(self.equipos, key=lambda x: x[5])
        print(f"A. Equipo que más goles anotó: {equipo_max_goles[0]}")
              
        equipo_max_puntos = max(self.equipos, key=lambda x: x[7])
        print(f"B. Equipo con más puntos: {equipo_max_puntos[0]}")

        equipo_max_partidos_ganados = max(self.equipos, key=lambda x: x[2])
        print(f"C. Equipo que más partidos ganó: {equipo_max_partidos_ganados[0]}")

        total_goles = sum(equipo[5] for equipo in self.equipos)
        print(f"D. Total de goles anotados por todos los equipos: {total_goles}")

        promedio_goles = total_goles / len(self.equipos)
        print(f"E. Promedio de goles anotados en el torneo: {promedio_goles}")

torneo = Torneo()
while True:
    print(titulo)
    print("\nMenú Principal:")
    print("1. Agregar Equipo\n2. Registro de Fecha y Partido\n3. Tabla de Posiciones\n4. Salir y Mostrar Reportes")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        torneo.agregar_equipo()
    elif opcion == "2":
        torneo.registrar_fecha_partido()
    elif opcion == "3":
        torneo.mostrar_tabla_posiciones()
    elif opcion == "4":
        torneo.reportes()
        break
    else:
        print("Opción no válida. Intente de nuevo.")
