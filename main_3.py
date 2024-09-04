 #  Elaborar um função em Python para ordenar uma lista utilizando a ordenação por 
# inserção (Insertion Sort). 

# def insertion_sort(list):
#     for j in range(1, len(list)):
#         key = list[j]
#         i = j - 1
        
#         while i >= 0 and list[i] > key:
#             list[i + 1] = list[i]
#             i -= 1
        
#         list[i + 1] = key

# list = [12, 5, 1, 200, 3, 956, 13]
# insertion_sort(list)
# print("Lista ordenada:", list)

# primeira parte
lista_a = [4, 2, 8, 6, 5]
lista_b = lista_a
lista_b[3] = 999
print(lista_a)
# segunda parte
lista_a = [4, 2, 8, 6, 5]
lista_b = lista_a[:]
lista_b[3] = 999
print(lista_a)

