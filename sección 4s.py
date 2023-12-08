# 1. Cree un programa que lea los tres ángulos internos de un triángulo y muestre si los ángulos corresponden a un triángulo o no.

angulo1 = float (input ('ingrese primer angulo :'))

angulo2 = float (input ('ingrese segundo angulo :'))

angulo3 = float (input ('ingrese tercer angulo :'))

suma = angulo1 + angulo2 + angulo3

if suma == 180 :
    print (" si corresponden a un triangulo")
else :
    print (" no corresponden a un triangulo")

print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 2. Cree un programa que lea un número y muestre si éste es par o impar.

numero = float(input('inresa el  numero :'))

if numero % 2 == 0 :
    print ('el numro es par')
else :
    print ('el numro es impar')

print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 3. Cree un programa que lea un número y muestre si éste es divisible entre cinco o no.

numero = float(input('ingresa el numero :'))

if numero % 5 == 0 :
    print("el numero",numero,"es divisble entre 5")
else :
    print('el numero',numero, 'no es divisble entre 5')

print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 4. Cree un programa que lea un número entre 1 y 15 y muestre si éste es primo o no

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingrese un número entre 1 y 15: "))

if 1 <= numero <= 15:
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.") 
else:
    print("Por favor, ingrese un número válido entre 1 y 15.")