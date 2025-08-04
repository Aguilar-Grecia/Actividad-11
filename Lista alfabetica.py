def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [i for i in lista[1:] if i <= pivote]
    iguales = [i for i in lista if i == pivote]
    mayores = [i for i in lista [1:] if i > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)

def main():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de nombres que desea registrar: "))
            if cantidad < 0:
                print("Por favor ingrese solamente numeros positivos. ")
            else:
                break
        except ValueError:
            print("Error, Por favor ingrese solamente numeros enteros. ")
    if cantidad ==0:
        print("No hay nombres ingresados para empezar a ordenar. ")
        return
    nombres = []
    print("\n Ingrese los nombres que desea registrar: ")
    for i in range(cantidad):
        nombre = input(f"Nombre {i+1}: ")
    nombres.append(nombre)
    nombres_ordenados = quick_sort(nombres)
    print("\n---Lista De Nombres Ordenados---")
    for nombre in nombres_ordenados:
        print(nombre)

if __name__ == '__main__':
    main()


