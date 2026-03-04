km = float(input("Ingresa la cantidad de kilómetros recorridos: "))
tiempo = float(input("Ingresa el tiempo en minutos: "))

if tiempo < 10 and km > 0:
    print("Valor a pagar: $ 5000")
elif tiempo >= 10:
    print("Valor a pagar: $", int(km * 800))
else:    print("ERROR ! ! Valor a pagar: $ 0")