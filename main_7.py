# Elaborar um programa Python para verifica se uma matriz 3x3 é simétrica. Uma
# matriz é dita simétrica se ela for igual a sua transposta. 

def verifica_simetria(matriz):
    transposta = [list(linha) for linha in zip(*matriz)]

    return matriz == transposta

matriz = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]

if verifica_simetria(matriz):
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")
