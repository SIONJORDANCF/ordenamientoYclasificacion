def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # Últimos i elementos ya están ordenados
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)

bubble_sort(numeros)

print("Lista ordenada:", numeros)