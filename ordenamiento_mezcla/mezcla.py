def merge_sort(lista):
    # Caso base: si la lista tiene un solo elemento, ya está ordenada
    if len(lista) > 1:
        # Encuentra el punto medio de la lista
        medio = len(lista) // 2
        izquierda = lista[:medio]  # Sublista izquierda
        derecha = lista[medio:]    # Sublista derecha

        # Llamadas recursivas para ordenar las dos mitades
        merge_sort(izquierda)
        merge_sort(derecha)

        # Inicializa índices para la fusión
        i = j = k = 0

        # Fusión de las dos sublistas ordenadas
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Si quedan elementos en la sublista izquierda
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Si quedan elementos en la sublista derecha
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

# Ejemplo de uso
numeros = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", numeros)

merge_sort(numeros)

print("Lista ordenada:", numeros)