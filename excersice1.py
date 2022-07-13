# Escriba un programa en Python que ingrese tres números enteros y calcule e imprima su suma. Sin embargo, si los tres números son todos iguales, imprima tres veces su suma.
num_1 = int(input("Ingrese el primer número -> "))
num_2 = int(input("Ingrese el segundo número -> "))
num_3 = int(input("Ingrese el tercer número -> "))
total = num_1+num_2+num_3

if num_1 != num_2 and num_3:
    print("La suma de los números ingresados es: "+str(total))
else:
    print(str(total))
    print(str(total))
    print(str(total))
