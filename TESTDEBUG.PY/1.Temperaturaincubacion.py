"""son muy sensibles a la temperatura y si se exponen más de 34°C no se desarrollan.
De la misma manera, temperaturas inferiores a 26°C no permiten que se
desarrollen los embriones.

“T. baja”, cuando la temperatura sea normal “T.
normal”, y cuando la temperatura sea muy alta, “T. alta”."""





def temp_(temperatura):
    if temperatura > 34:
        print ("Temperatura alta")
    elif temperatura < 26:
        print ("Temperatura  baja")
    else:
        print ("Temperatura normal")


temperatura = int(input("Ingrese temperatura en grados celsius: "))
temp_(temperatura)