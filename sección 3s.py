# 1. Cree un programa que lea la edad de un usuario e imprima un mensaje que diga si el usuario es mayor de edad o no

edad = float(input('ingrese su edad :'))

if edad >= 18 :
    print ('es mayor de edad')
else :
    print ('es menor de edad')


print ("--------------------------------------------------------------------------------------------------------------------------------------------")


""" 
    2. En un supermercado se tiene los siguientes productos: lentejas, crema, arroz y vino. Las lentejas y el arroz no
pagan IVA, el vino y la crema si. Cree un programa que reciba el nombre de alguno de los productos
mencionados y muestre si el producto paga IVA o no.

"""

print('--------super mercado--------')

producto = input ('ingrese producto :')

if producto == 'lentejas' or producto == 'arroz' or producto == 'crema' or producto == 'vino':

    if producto == 'lentejas' or producto == 'arroz':
        print('no paga iva')
    else:
        print('paga iva')
else:
    print('ingrese un producto valido')


print ("--------------------------------------------------------------------------------------------------------------------------------------------")



# 3. Cree un programa que reciba dos números y muestre el mayor. En caso de que los números sean iguales también se debe mostrar al usuario.

n1 = float(input (" ingrese el primer numero: "))
n2 = float(input (" ingrese el segundo numero: "))

if n1 > n2 :
    print (f" {n1} es mayor que {n2} " )
    print (f" {n2} es menor que {n1} ")
elif n1 < n2 :
     print (f" {n1} es menor que {n2}")
     print (f"{n2} es mayor que {n1} ") 
else:
     print ("ambosnumeros son iguales")


print ("--------------------------------------------------------------------------------------------------------------------------------------------")


# 4. Cree un programa que reciba tres números y muestre el mayor. En caso de que los números sean iguales también se debe mostrar al usuario.

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número:"))

if n1 == n2 == n3:
    print("Los tres números son iguales.")
else:
 
    mayor = max(n1, n2, n3)

 
    menor = min(n1, n2, n3)

 
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")






