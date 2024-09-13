# Elaborar um programa em Python para ordenar uma lista utilizando o algoritmo
# Bubble Sort.

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        troca_ocorrida = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                troca_ocorrida = True
        if not troca_ocorrida:
            break

lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
bubble_sort(lista)
print("Lista ordenada:", lista)
