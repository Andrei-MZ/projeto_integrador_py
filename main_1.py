#  Elaborar um programa Python para imprimir os divisores de um número.

def dividers(num):
    for i in range(1, num//2+1):
        if num % i == 0: 
            yield i
    yield num

num = int(input("Digite um numero para saber seu divisor: "))
print(list(dividers(num)))
