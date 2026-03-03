sueldo = float(input("Ingresa tu sueldo del mensual: $"))
imp_bajo = 0.05
imp_alto = 0.10
if sueldo < 1500000:
    print("No paga impuesto")
elif sueldo > 1500000 and sueldo <= 3000000:
    print("Paga impuesto 5%:", sueldo * imp_bajo, "Tu sueldo neto es de: $ ", sueldo - (sueldo * imp_bajo))
elif sueldo >= 3000001:
    print("Paga impuesto 10%:", sueldo * imp_alto, "Tu sueldo neto es de: $ ", sueldo - (sueldo * imp_alto))
else:
    print("No paga impuesto, tu sueldo es de: $", sueldo)
