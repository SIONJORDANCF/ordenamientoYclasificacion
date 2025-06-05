def selection_sort(lista):
    n = len(lista)
    
    # Recorremos toda la lista
    for i in range(n):
        # Encuentra el índice del valor mínimo en el resto de la lista
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        
        # Intercambia el elemento mínimo con el primer elemento no ordenado
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

# Ejemplo de uso
numeros = [64, 25, 12, 22, 11]
print("Lista original:", numeros)

selection_sort(numeros)

print("Lista ordenada:", numeros)