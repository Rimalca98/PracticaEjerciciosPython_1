usuario = input("Ingrese su nombre: ")
contraseña = input("Ingrese su contraseña: ")
if usuario == "admin" and contraseña == "1234":
    print("Acceso concedido.")
else:
    print("Acceso denegado.")