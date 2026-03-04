edad = int(input("Ingrese su edad: "))
estrato = int(input("Ingrese su estrato social: "))
if edad > 18 and edad < 25:
    if estrato >= 1 and estrato <= 3:
        print("Aplica para subsidio.")
    else:
        print("No aplica para subsidio.")
if edad > 0 and edad < 18 or edad >= 25 and edad <= 60:
    print("No aplica para subsidio.")
    #