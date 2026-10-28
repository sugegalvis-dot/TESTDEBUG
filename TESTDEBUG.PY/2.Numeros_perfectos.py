
def num_perfecto(num):
    suma = 0
    for i in range (1,num):
        if num % i ==0:
            suma= suma + i
    return suma



num = int(input("Ingrese un numero: "))


while num >=0: 
    if num > 2:
        if num_perfecto(num) == num:
            print ("Es un número perfecto")
        else:
            print ("NO es un numero perfecto")
    else: 
        print ("El número debe ser mayor que 2")

    num = int(input("Ingrese otro numero: "))

print ("Programa finalizado")




