try:
    numero = int(input("Ingrese un número entero: "))
except ValueError:
    print("Error: No se aceptan decimales o texto, solo numeros enteros")
else:
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print("El número", numero, " no es múltiplo de 3 ni de 5")