def calcular_pago(tipo_empleado, horas_trabajadas):
    if tipo_empleado == 1:
        pago_por_hora = 20000
    else:
        pago_por_hora = 10000

    total_pago = horas_trabajadas * pago_por_hora
    return total_pago

tipo_empleado = int(input("Ingrese el tipo de empleado (1: Planta, 2: Administrativo): "))
horas_trabajadas = float(input("Ingrese el total de horas trabajadas: "))

total_pago = calcular_pago(tipo_empleado, horas_trabajadas)
print("El total de pago es:", total_pago)
