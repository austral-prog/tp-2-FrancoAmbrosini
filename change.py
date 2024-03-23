def change():
    expense=float(input("ingresar gasto:"))
    print()
    money=float(input("dinero recibido: "))
    vuelto= money-expense
    pesos= int(vuelto)
    centavos= int(100*(vuelto-pesos))
    print()
    print("pesos: ",pesos)
    print()
    print("centavos: ",centavos)
