def separate_numbers(lista):
    positivos = [num for num in lista if num >= 0]
    negativos = [num for num in lista if num < 0]

    return positivos, negativos

numeros = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))

positivos, negativos = separate_numbers(numeros)

print("Números Positivos:", positivos)
print("Números Negativos:", negativos)