def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [i for i in lista[1:] if i <= pivote]
    iguales = [i for i in lista if i == pivote]
