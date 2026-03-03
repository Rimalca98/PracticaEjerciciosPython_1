producto = int(input("Ingrese el precio del producto: "))
iva = producto * 0.19

print(f"Valor bruto: ${producto: .2f}")
print(f"Valor IVA: ${iva: .2f}")
print(f"Valor total: ${producto + iva: }")
