temperatura = int(input("Ingrese la temperatura: "))
presion = int(input("Ingrese la presión: "))

if presion > 200 or temperatura > 100:
    print("Alarma")
else:
    print("Normal")
