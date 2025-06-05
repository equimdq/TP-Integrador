from random import randint


# Cada función genera una lista de 30.000 elementos
def generar_lista_aleatoria():
    return [randint(1, 30000) for _ in range(30000)]

def generar_lista_ordenada():
    return list(range(1, 30001))

def generar_lista_ordenada_inver():
    return list(range(30000, 0, -1))


def generar_lista():
    print("\nElija el tipo de lista:")
    print("1. Aleatoria")
    print("2. Ordenada")
    print("3. Ordenada invertida")

    while True:
        opcion = input("\nOpción: ").strip()
        if opcion in ["1", "2", "3"]:
            match opcion:
                case "1":
                    lista = generar_lista_aleatoria()
                case "2":
                    lista = generar_lista_ordenada()
                case "3":
                    lista = generar_lista_ordenada_inver()

            print("\nLista generada con 30.000 elementos.")
            # Mostramos un preview opcional
            print(f"Inicio: {lista[:5]} ... {lista[-5:]} Fin.\n")
            return lista
        else:
            print("Opción no válida. Intente nuevamente.")
