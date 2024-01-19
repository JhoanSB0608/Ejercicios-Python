titulo = """
    ++++++++++++++++++++++++++++++++++++++++++
    +   Proyecto Liga Colombiana De Futbol   +
    ++++++++++++++++++++++++++++++++++++++++++
"""
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.PJ = 0
        self.PG = 0
        self.PP = 0
        self.PE = 0
        self.GF = 0
        self.GC = 0
        self.TP = 0

class Torneo:
    def __init__(self):
        self.equipos = []

    def agregar_equipo(self):
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        equipo = Equipo(nombre_equipo)
        self.equipos.append(equipo)
        print(f"Equipo {nombre_equipo} registrado con éxito.")

    def registrar_fecha_partido(self):
        fecha = input("Ingrese la fecha: ")
        for _ in range(1):
            local = input("Ingrese el nombre del equipo local: ")
            visitante = input("Ingrese el nombre del equipo visitante: ")
            goles_local = int(input(f"Ingrese los goles anotados por {local}: "))
            goles_visitante = int(input(f"Ingrese los goles anotados por {visitante}: "))
            self.actualizar_tabla(local, visitante, goles_local, goles_visitante)
        print(f"Fecha {fecha} registrada con éxito.")

    def actualizar_tabla(self, local, visitante, goles_local, goles_visitante):
        equipo_local = next(equipo for equipo in self.equipos if equipo.nombre == local)
        equipo_visitante = next(equipo for equipo in self.equipos if equipo.nombre == visitante)

        equipo_local.PJ += 1
        equipo_visitante.PJ += 1

        if goles_local > goles_visitante:
            equipo_local.PG += 1
            equipo_local.TP += 3
            equipo_visitante.PP += 1
        elif goles_local < goles_visitante:
            equipo_visitante.PG += 1
            equipo_visitante.TP += 3
            equipo_local.PP += 1
        else:
            equipo_local.PE += 1
            equipo_local.TP += 1
            equipo_visitante.PE += 1
            equipo_visitante.TP += 1

        equipo_local.GF += goles_local
        equipo_local.GC += goles_visitante

        equipo_visitante.GF += goles_visitante
        equipo_visitante.GC += goles_local

    def mostrar_tabla_posiciones(self):
        print("\nTabla de Posiciones:")
        print("----------------------------------------------------------------")
        print("----------------------------------------------------------------")
        for equipo in self.equipos:
            print("Equipo\t\t\t\t\t\t\tPJ\tPG\tPE\tPP\tGF\tGC\tTP")
            print(f"{equipo.nombre}\t{equipo.PJ}\t{equipo.PG}\t{equipo.PE}\t{equipo.PP}\t{equipo.GF}\t{equipo.GC}\t{equipo.TP}")
            print("----------------------------------------------------------------")

    def reportes(self):
        equipo_max_goles = max(self.equipos, key=lambda x: x.GF)
        print(f"A. Equipo que más goles anotó: {equipo_max_goles.nombre}")
              
        equipo_max_puntos = max(self.equipos, key=lambda x: x.TP)
        print(f"B. Equipo con más puntos: {equipo_max_puntos.nombre}")

        equipo_max_partidos_ganados = max(self.equipos, key=lambda x: x.PG)
        print(f"C. Equipo que más partidos ganó: {equipo_max_partidos_ganados.nombre}")

        total_goles = sum(equipo.GF for equipo in self.equipos)
        print(f"D. Total de goles anotados por todos los equipos: {total_goles}")

        promedio_goles = total_goles / len(self.equipos)
        print(f"E. Promedio de goles anotados en el torneo: {promedio_goles}")


# Menú principal
torneo = Torneo()
while True:
    print(titulo)
    print("\nMenú Principal:")
    print("1. Agregar Equipo")
    print("2. Registro de Fecha y Partido")
    print("3. Tabla de Posiciones")
    print("4. Salir y Mostrar Reportes")

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