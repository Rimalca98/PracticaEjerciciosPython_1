print("================================")
print("Bienvenido al Cajero Automático")
print("================================")

print("1. Consultar saldo")
print("2. Retirar dinero")
print("3. Depositar dinero")

saldo = 1000

opcion = int(input("Seleccione una opción: "))

while opcion < 1 or opcion > 3:
    print ("Opción no válida.")
    opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    print(f"Su saldo actual es de:  ${saldo}")

elif opcion == 2:
    print("Usted ha seleccionado retirar dinero.")
    retiro = int(input("Que cantidad va a retirar? $ "))

    while retiro <= 0 or retiro > saldo:
        if retiro <= 0:
            print("Monto invalido, Ingrese un monto valido...")
        else:
            print(f"Saldo insuficiente, tu saldo es de: {saldo}")
        retiro = int(input("Que cantidad desea retirar: $ "))
    saldo -= retiro
    print(f"Transaccion completada, su nuevo saldo es de: $ {saldo}")
                 


elif opcion == 3:
    print("Usted ha seleccionado depositar dinero.")
    deposito = int(input("Que cantidad va a depositar? $ "))    
    
    while deposito <= 0:
        print("Monto invalido, Ingrese un monto valido...")
        deposito = int(input("Que cantidad va a depositar? $ "))
    saldo += deposito
    print(f"Deposito correcto, nuevo saldo: $ {saldo}")
        
input("\nGracias por usar el cajero automático. Presiona Enter para salir...")
                


