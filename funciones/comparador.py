from funciones.algoritmos import *
from funciones.generador_listas import generar_lista


def comparar_algoritmos():
    print("\n=== COMPARADOR DE ALGORITMOS DE ORDENAMIENTO ===")

    while True:
        print("\nElige un algoritmo:")
        print("1. Ordenamiento por selección")
        print("2. Ordenamiento por inserción")
        print("3. Ordenamiento burbuja")
        print("4. Ordenamiento rápido (quicksort)")
        print("5. Comparar todos los algoritmos")
        print("6. Salir")

        opcion = input("\nOpción: ").strip()

        if opcion in ["1", "2", "3", "4", "5"]:
            # Generar la lista
            lista_original = generar_lista()

            if opcion == "1":
                print("\n--- Ejecutando Ordenamiento por selección ---")
                lista_copia = lista_original.copy()
                ordenamiento_seleccion(lista_copia)
                print("Ordenamiento completado.")

            elif opcion == "2":
                print("\n--- Ejecutando Ordenamiento por inserción ---")
                lista_copia = lista_original.copy()
                ordenamiento_insercion(lista_copia)
                print("Ordenamiento completado.")

            elif opcion == "3":
                print("\n--- Ejecutando Ordenamiento burbuja ---")
                lista_copia = lista_original.copy()
                ordenamiento_burbuja(lista_copia)
                print("Ordenamiento completado.")

            elif opcion == "4":
                print("\n--- Ejecutando Ordenamiento rápido ---")
                lista_copia = lista_original.copy()
                ordenamiento_rapido(lista_copia)
                print("Ordenamiento completado.")

            elif opcion == "5":
                print("\n--- Ejecutando todos los algoritmos ---")

                print("\nEjecutando Ordenamiento por selección...")
                lista_copia = lista_original.copy()
                ordenamiento_seleccion(lista_copia)
                print("Ordenamiento por selección completado.")

                print("\nEjecutando Ordenamiento por inserción...")
                lista_copia = lista_original.copy()
                ordenamiento_insercion(lista_copia)
                print("Ordenamiento por inserción completado.")

                print("\nEjecutando Ordenamiento burbuja...")
                lista_copia = lista_original.copy()
                ordenamiento_burbuja(lista_copia)
                print("Ordenamiento burbuja completado.")

                print("\nEjecutando Ordenamiento rápido...")
                lista_copia = lista_original.copy()
                ordenamiento_rapido(lista_copia)
                print("Ordenamiento rápido completado.")

        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

