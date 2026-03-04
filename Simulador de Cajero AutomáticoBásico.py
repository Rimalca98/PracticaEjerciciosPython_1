print("================================")
print("Bienvenido al Cajero Automático")
print("================================")

print("1. Consultar saldo")
print("2. Retirar dinero")
print("3. Depositar dinero")

saldo = 1000

opcion = input("Seleccione una opción: ")

if opcion == "1":
    print("Su saldo actual es de:  $", saldo)
elif opcion == "2":
    print("Usted ha seleccionado retirar dinero.")
    retiro = int(input("Que cantidad va a retirar? $ "))
    if retiro > 1000:
        print("Fondos Insuficientes...")
    
    if retiro < 0:
        print("Ingrese un monto valido...")
        
    else:
        print("Transaccion completada!")
        print("Su nuevo saldo es de: $", saldo - retiro )


elif opcion == "3":
    print("Usted ha seleccionado depositar dinero.")
else:
    print("Opción no válida.")
