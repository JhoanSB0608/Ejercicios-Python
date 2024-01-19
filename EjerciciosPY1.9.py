precio_base = float(input("Ingrese el valor de precio base: "))

if precio_base > 150000:
    impuesto = precio_base * 0.19
else:
    impuesto = precio_base * 0.16

print("El impuesto a pagar es:", impuesto)
