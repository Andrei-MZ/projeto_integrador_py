 #  Elaborar um função em Python para ordenar uma lista utilizando a ordenação por 
# inserção (Insertion Sort). 

def insertion_sort(list):
    for j in range(1, len(list)):
        key = list[j]
        i = j - 1
        
        while i >= 0 and list[i] > key:
            list[i + 1] = list[i]
            i -= 1
        
        list[i + 1] = key

list = [9, 5, 1, 4, 3]
insertion_sort(list)
print("Lista ordenada:", list)

