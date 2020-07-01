def esprimo(numero):...

def ejercicios(num):

    if num > 0:
         s = "El numero es positivo"

    elif num < 0:
        s = "El numero es negativo"

    else:
        s = "El numero es cero"

    print(s)

    if num % 2:
        p = "El numero es impar"

    else:
        p = "El numero es par"

    print(p)

    if esprimo(num):
        primo = "El numero es primo"
    else:
        primo = "El numero no es primo"

        print(primo)

if __name__=='__main__':
    print("Ingrese un numero: ")
    try:
        inp = int(input())

    except ValueError:
        print("El dato ingresado no es un entero")

    ejercicios(inp)

    print("\nIngrese un año:")
    año = int(input())

    if año < 0:
        print("El año no es valido")

    if año%4:
        print(año, "no es un año bisiesto")
    elif año%100:
        print(año, "es un año bisiesto")
    elif año%400:
        print(año, "no es un año bisiesto")
    else:
        print(año, "es un año bisiesto")
