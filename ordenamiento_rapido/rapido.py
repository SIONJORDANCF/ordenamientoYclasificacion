def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        # Elegir un pivote (en este caso, el último elemento)
        pivote = lista[-1]
        
        # Sublistas de elementos menores y mayores que el pivote
        menores = [x for x in lista[:-1] if x <= pivote]
        mayores = [x for x in lista[:-1] if x > pivote]
        
        # Recursivamente ordenamos las sublistas y las combinamos con el pivote
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Ejemplo de uso
numeros = [10, 7, 8, 9, 1, 5]
print("Lista original:", numeros)

numeros_ordenados = quick_sort(numeros)

print("Lista ordenada:", numeros_ordenados)