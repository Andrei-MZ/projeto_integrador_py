def separate_numbers(lista):
    positivos = [num for num in lista if num >= 0]
    negativos = [num for num in lista if num < 0]

    return positivos, negativos

numeros = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))