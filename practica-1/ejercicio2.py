name = input("¿Cual es tu nombre? ")
input (name + " ¿Cual es tu edad? ")
print("Ingresa tus 5 notas")
note1 = float(input("Nota1: "))
note2 = float(input("Nota2: "))
note3 = float(input("Nota3: "))
note4 = float(input("NOta4: "))
note5 = float(input("NOta5: "))
promedio = (note1 + note2 + note3 + note4 + note5) / 5
if promedio < 3:
    print(name + " haz perdido la materia: ", promedio)
elif promedio >= 3:
    print(name + " ganaste la materia: ", promedio)
print("fin")
 
