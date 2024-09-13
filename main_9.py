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

# ou somar matriz 1 e matriz 2 "\n"

def cria_matriz(n_linhas, n_colunas, valor): 
    matriz = [] 
    for _ in range(n_linhas):
        linha = [valor] * n_colunas
        matriz.append(linha)
    return matriz    

def soma_matrizes(m1, m2):
    num_lin = len(m1)
    num_col = len(m1[0])

    num_linB = len(m2)
    num_colB = len(m2[0])

    if num_lin == num_linB and num_col == num_colB:
        C = cria_matriz(num_lin, num_col, 0)

        for lin in range(num_lin):
            for col in range(num_col):
                C[lin][col] = m1[lin][col] + m2[lin][col]
                
        return C
    else:
        return False
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

resultado = soma_matrizes(matriz1, matriz2)

if resultado:
    print("\n Matriz resultante da soma:\n" )
    for linha in resultado:
        print(linha)
else:
    print("As matrizes têm dimensões diferentes e não podem ser somadas.")

