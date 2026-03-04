ancho = float(input("Ingrese el ancho del cuarto en metros: "))
largo = float(input("Ingrese el largo del cuarto en metros: "))
area = ancho * largo
if area > 0 and area < 12:
    print("El cuarto es pequeño. Área:", area)
elif area >= 12 and area <= 20:
    print("El cuarto es mediano. Área:", area)
else:
    print("El cuarto es grande. Área:", area)