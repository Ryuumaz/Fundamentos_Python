'''
14. Faça um programa para converter euros para dólares e vice-versa. Pesquise o câmbio actual ou utilize o
seguinte: €1 → $1,39. O programa deverá por começar por perguntar qual o sentido da conversão,
apresentando depois a conversão. Exemplo:

    Escolha o sentido da conversão
    1. Euros -> Dólares
    2. Dólares -> Euros
    T. Terminar
    > 2
    Montante em dólares: 2000
    Euros -> 1438.85
'''
from decimal import Decimal as dec

def main():
    while True:
        print("Escolha o sentido da conversão")
        print("1. Euros -> Dólares")
        print("2. Dólares -> Euros")
        print("T. Terminar")
        opt = input("Opção: ")

        if opt == "T" or opt == "t":
            print("O programa terminou.")
            break
        
        match(opt):
            case '1':
                euro = dec(input("Indica a quantidade em Euro: "))
                dolar = euro*dec(1.08)
                print(f"Convertido: {euro:.2f}€ -> {dolar:.2f}$\n")
            case '2':
                dolar = dec(input("Indica a quantidade em Dolar: "))
                euro = dolar*dec(0.92)
                print(f"Convertido: {dolar:.2f}$ -> {euro:.2f}€\n")
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()