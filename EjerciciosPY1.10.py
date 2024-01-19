sueldo_anual = 144000000

años_en_empresa = int(input("Ingrese los años que lleva en la empresa: "))

if años_en_empresa >= 10:
        sueldo_final = sueldo_anual + (sueldo_anual * 0.10)
elif años_en_empresa > 5:
        sueldo_final = sueldo_anual + (sueldo_anual * 0.07)
elif años_en_empresa > 3:
        sueldo_final = sueldo_anual + (sueldo_anual * 0.05)
else:
        sueldo_final = sueldo_anual + (sueldo_anual * 0.03)

print("El sueldo final del trabajador es:", sueldo_final)