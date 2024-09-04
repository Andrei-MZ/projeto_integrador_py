# Elaborar um programa Python para intercalar duas listas ordenadas. 

lista1 = ['um','dois','três','quatro','cinco']
lista2 = [1,2,3,4,5]

lista3 = []
for index in range(len(lista1)):
    lista3.append(lista1[index])
    lista3.append(lista2[index])

print(lista3)


# Ou podemos usar o "set"  que é uma coleção ordenada de elementos unicos, no caso se tiver elementos duplicados são removidos automaticamente

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list_result = list(set(list1 + list2))

print(list_result)

 