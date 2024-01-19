contraseña_correcta = "contraseña123"

contraseña_ingresada = input("Ingrese su contraseña: ")

if contraseña_ingresada == contraseña_correcta:
    print("Bienvenido, acceso concedido.")
else:
    print("Error: Contraseña incorrecta. Acceso denegado.")
