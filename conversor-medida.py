# Solicitar entrada del usuario con validación
while True:
    try:
        medida_cm = float(input("Ingrese la medida de la pieza en cm: "))
        if medida_cm < 0:
            print("La medida no puede ser negativa.")
            continue
        break
    except ValueError:
        print("El dato ingresado no es válido.")

# Calcular y mostrar resultado
conversion_cm_pulgadas = medida_cm / 2.54

print(f"{medida_cm} cm de la pieza son {conversion_cm_pulgadas:.2f} pulgadas")