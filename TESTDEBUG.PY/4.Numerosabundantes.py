def suma_divisores(num):
    suma = 0
    for i in range(1, num):        
        if num % i == 0:
            suma += i
    return suma

inicial = int(input("Rango inicial: "))
final = int(input("Rango final: "))

if inicial > final:
    print("El rango inicial no puede ser mayor que el final")
else:
    abundantes = []

    for num in range(inicial, final + 1):    
        if suma_divisores(num) > num:
            abundantes.append(num)

    print("Los números abundantes entre", inicial, "y", final, "son:")
    print(abundantes)
    