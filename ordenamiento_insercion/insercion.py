def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

# Ejemplo de uso
numeros = [12, 11, 13, 5, 6]
print("Lista original:", numeros)

insertion_sort(numeros)

print("Lista ordenada:", numeros)