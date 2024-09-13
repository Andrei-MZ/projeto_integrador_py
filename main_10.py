# Elaborar uma função em Python para computar o maior e o menor elemento de
# uma lista. 

def maior_e_menor_elemento(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    
    maior = max(lista)
    menor = min(lista)

    return maior, menor

# Exemplo de uso
lista = [8, 1, 2, 3, 7, 5]
maior, menor = maior_e_menor_elemento(lista)
print("Maior elemento:", maior)
print("Menor elemento:", menor)
