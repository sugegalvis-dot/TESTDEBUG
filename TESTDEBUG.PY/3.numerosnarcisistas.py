def num_narcisista (num):
    temp = num 
    cantidad_digitos = 0

    while num > 0:
        cantidad_digitos += 1
        num = num // 10

    suma = 0 
    num = temp

    while num > 0:
        digito = num % 10 
        suma += digito ** cantidad_digitos
        num = num // 10 

    return suma == temp

num = int(input("Ingrese un número"))

while num > 0: 
    if num_narcisista(num):
        print ("Es un número narcisista")
    else: 
        print ("NO es un número narcisista")

    num = int(input("Ingrese otro número: "))

print ("Programa finalizado")

    