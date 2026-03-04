precio = float(input("Ingresa el precio del producto: $"))
if precio > 100000:
    print("Producto con descuento:", precio - (precio * 0.10))
else:
    print("Producto sin descuento: $", precio)