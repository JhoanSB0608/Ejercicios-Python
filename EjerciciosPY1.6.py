def calcular_pagos_restaurante():
    total_consumo = float(input("Ingrese el monto total del consumo en el restaurante: "))
    
    descuento = 0.15 * total_consumo if total_consumo > 130000 else 0
    total_con_descuento = total_consumo - descuento

    print("Monto total del consumo:", total_consumo)
    print("Descuento aplicado:", descuento)
    print("Monto total con descuento:", total_con_descuento)
calcular_pagos_restaurante()
