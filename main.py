from ordenamiento_burbuja.burbuja import bubble_sort
from ordenamiento_insercion.insercion import insertion_sort
from ordenamiento_mezcla.mezcla import merge_sort
from ordenamiento_rapido.rapido import quick_sort
from ordenamiento_seleccion.seleccion import selection_sort

def mostrar_menu():
    print("\n------ Menú de Ordenamientos ------")
    print("1. Ordenamiento por Burbuja")
    print("2. Ordenamiento por Inserción")
    print("3. Ordenamiento por Mezcla")
    print("4. Ordenamiento Rápido")
    print("5. Ordenamiento por Selección")
    print("6. Salir")
    print("----------------------------------")

def main():
    lista = [80,20,10,5,15,6,3]

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            print("\nOrdenando por Burbuja...")
            print(bubble_sort(lista))
        elif opcion == '2':
            print("\nOrdenando por Inserción...")
            print(insertion_sort(lista))
        elif opcion == '3':
            print("\nOrdenando por Mezcla (Merge Sort)...")
            print(merge_sort(lista))
        elif opcion == '4':
            print("\nOrdenando por Rápido (Quick Sort)...")
            print(quick_sort(lista))
        elif opcion == '5':
            print("\nOrdenando por Selección...")
            print(selection_sort(lista))
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()