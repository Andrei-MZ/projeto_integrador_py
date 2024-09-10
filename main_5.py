def separate_numbers(list):
    positivos = [num for num in lista if num >= 0]
    negativos = [num for num in lista if num < 0]

    return positivos, negativos