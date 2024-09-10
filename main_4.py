def tabela_verdade_xor():
    print("A | B | A XOR B")
    print("--|---|--------")
    for a in [0, 1]:
        for b in [0, 1]:
            resultado = a ^ b 
            print(f"{a} | {b} |    {resultado}")

tabela_verdade_xor()
