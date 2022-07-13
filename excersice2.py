grade = int(input("Ingresa el numero para decirte tu grado: "))
if grade >= 90:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60 <= grade < 70:
    print("D")
elif 60 < grade:
    print("F")
