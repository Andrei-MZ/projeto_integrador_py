# Elaborar um programa Python para gerar a tabela verdade do “ou exclusivo”.

def truth_table_xor():
    print("A | B | A XOR B")
    print("--|---|--------")
    for a in [0, 1]:
        for b in [0, 1]:
            resultado = a ^ b 
            print(f"{a} | {b} |    {resultado}")

truth_table_xor()
