nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 0 and promedio < 55:
    print("Reprobado, tu promedio es de: ", promedio)
elif promedio >= 55 and promedio < 60:
    print("Va a habilitacion, tu promedio es: ", promedio)
elif promedio >= 60 and promedio <= 100:
    print("Aprobado, tu promedio es: ", promedio)
else:    
    print("Promedio no valido")