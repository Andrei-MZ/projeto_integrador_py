# Elaborar um programa Python para realizar a soma dos elementos de uma matriz
# N por N. 


def soma_matriz(matriz):
    soma = 0
    for linha in matriz:
        soma += sum(linha)
    return soma

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")
for linha in matriz:
    print(linha)

resultado = soma_matriz(matriz)
print("\nSoma total dos elementos da matriz 1:", resultado) 


