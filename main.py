from funciones.comparador import comparar_algoritmos


def mostrar_menu():
    """ Muestra el menú inicial del programa """
    print("=== COMPARADOR DE ALGORITMOS DE ORDENAMIENTO ===")
    print("\nElija una opción:")
    print("1. Comparar algoritmos")
    print("2. Como usar el programa")
    print("3. Salir")


def mostrar_instrucciones():
    """ Muestra las instrucciones de uso del programa """
    print("\n" + "="*60)
    print("INSTRUCCIONES DE USO")
    print("="*60)
    print("Este programa te permite comparar diferentes algoritmos de ordenamiento:")
    print("\n• Algoritmos disponibles:")
    print("  - Ordenamiento por selección")
    print("  - Ordenamiento por inserción") 
    print("  - Ordenamiento burbuja")
    print("  - Ordenamiento rápido (quicksort)")
    print("\n• Tipos de listas para probar:")
    print("  - Lista aleatoria (30,000 elementos)")
    print("  - Lista ya ordenada (1 a 30,000)")
    print("  - Lista ordenada invertida (30,000 a 1)")
    print("\n• Puedes probar un algoritmo individual o compararlos todos")
    print("• Cada algoritmo trabaja con su propia copia de la lista")
    print("\nPresiona Enter para continuar...")
    input()


def main():
    """ Función principal del programa """
    while True:
        mostrar_menu()

        opcion = input("\nIngrese una opción (1-3): ").strip()

        match opcion:
            case "1":
                comparar_algoritmos()
                print("Regresando al menú principal...\n")
            case "2":
                mostrar_instrucciones()
            case "3":
                print("\nSaliendo...")
                print("Gracias por usar el programa. ¡Hasta luego!.\n")
                break
            case _:
                print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()
 