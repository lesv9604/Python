anio = int(input("Ingrese un año: "))

resultado = anio % 4

if resultado == 0:
    print("Este año es bisiesto")
else:
    print("Este año no es bisiesto")
