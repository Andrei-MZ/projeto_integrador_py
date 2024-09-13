# Elaborar um programa Python para calcular a união e a intersecção entre dois
# conjuntos.

def intersecao(conjuntoA, conjuntoB):
    inter = [x for x in range(1, 12) if x in conjuntoA and x in conjuntoB]
    return inter

a = [2, 4, 6, 7, 10]
b = [3, 4, 6, 8, 10, 11]
print(intersecao(a, b))
