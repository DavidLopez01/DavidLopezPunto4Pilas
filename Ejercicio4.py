def buscarPila():
    pila = []

    while True:
        if not pila:
            print("La pila está vacia, se debe llenar")
            pila = input("Introduzca los elementos de la pila separados por espacios, por favor: ").split()
        
        print("\nPila actual: ", pila)

        valor1 = input("Introduce el elemento a buscar: ")

        if valor1 in pila:
            posicion = len (pila) - pila.index(valor1)
            print(f"\n El elemento '{valor1}' estaba en la posición {posicion} desde la cima de la pila")
            break
        else:
            print(f"\nEl elemento '{valor1}' no está en la pila, intente otra vez.")

buscarPila()