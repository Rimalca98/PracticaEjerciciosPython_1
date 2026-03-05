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
    print("Su saldo actual es de:  $", saldo)
    input("Gracias por usar el cajero automático, presiona enter para salir...")

elif opcion == 2:
        print("Usted ha seleccionado retirar dinero.")
        retiro = int(input("Que cantidad va a retirar? $ "))

        while retiro <= 0:
            print("Monto invalido, Ingrese un monto valido...")
            retiro = int(input("Que cantidad va a retirar? $ "))

        while retiro > saldo:
            print("Fondos Insuficientes...")
            retiro = int(input("Que cantidad va a retirar? $ "))    
            if retiro < 0:
                print("Ingrese un monto valido...")
        
        else:
            print("Transaccion completada!")
            print("Su nuevo saldo es de: $", saldo - retiro )
            input("Gracias por usar el cajero automático, presiona enter para salir...")


elif opcion == 3:
    print("Usted ha seleccionado depositar dinero.")
    deposito = int(input("Que cantidad va a depositar? $ "))    
    
    while deposito <= 0:
            print("Monto invalido, Ingrese un monto valido...")
            deposito = int(input("Que cantidad va a depositar? $ "))
    if deposito > 0:
        print(f"Deposito correcto, nuevo saldo: $ {saldo + deposito}")
        input("Gracias por usar el cajero automático, presiona enter para salir...")
                


