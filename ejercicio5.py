numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
suma = numero1 + numero2
print("La suma de",  numero1 + numero2 , "es", suma, ".")
resta = numero1 - numero2
print("La resta de", numero1, "y", numero2, "es", resta, ".")
multiplicacion = numero1 * numero2
print("La multiplicación de", numero1, "y", numero2, "es", multiplicacion, ".")
if numero2 != 0:
    division = numero1 / numero2
    print("La división de", numero1, "y", numero2, "es", division, ".")
else:
    print("No se puede dividir por cero.")
    