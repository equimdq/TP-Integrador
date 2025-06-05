def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        indice_min = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        lista[i], lista[indice_min] = lista[indice_min], lista[i]
    return lista


def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > temp:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = temp
    return lista


def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


def ordenamiento_rapido(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    izq = [x for x in lista if x < pivot]
    medio = [x for x in lista if x == pivot]
    der = [x for x in lista if x > pivot]
    return ordenamiento_rapido(izq) + medio + ordenamiento_rapido(der)