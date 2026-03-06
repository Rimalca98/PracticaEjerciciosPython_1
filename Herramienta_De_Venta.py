print("="*35)
print("Herramienta de ventas RiwiTechStore")
print("="*35)


nombre = input("Ingrese el nombre del cliente: ")

precio_unidad = int(input("Precio por unidad: $"))
cantidad = int(input("Cantidad de productos: "))

soli_vip = input("El usuario tiene VIP, favor responder s/n en minuscula: ")
vip = soli_vip == "s"

desc_vip = 0.10

subtotal = precio_unidad * cantidad
descuento = subtotal * desc_vip if vip else 0.0
total = subtotal - descuento

print("\nResumen de la Venta")
print(f"\nNombre del cliente: {nombre}")
print(f"Cantidad: {cantidad} unidad(es) x {precio_unidad:,}")
print(f"Subtotal: {subtotal:,}")

if vip:
    print(f"Menos Descuento por VIP: {descuento:,} (10% aplicado)")
else:
    print("No aplica DESCUENTO VIP\n")

print(f"Total a pagar: $ {total:,}")

#

