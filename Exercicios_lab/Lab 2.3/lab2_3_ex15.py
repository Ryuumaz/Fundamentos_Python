'''
15. Remova a opção 'T' para terminar o programa. Agora, no final de uma conversão, o programa
questiona o utilizador se pretende realizar nova conversão:
    
    Escolha o sentido da conversão
    1. Euros -> Dólares
    2. Dólares -> Euros
    > 2

    Montante em dólares: 2000
    Euros -> 1438.85
    Pretende efecturar mais conversões (S/N)? n
    Fim do programa
'''
from decimal import Decimal as dec

def main():
    while True:
        print("\nEscolha o sentido da conversão")
        print("1. Euros -> Dólares")
        print("2. Dólares -> Euros")
        opt = input("Opção: ")
        
        match(opt):
            case '1':
                euro = dec(input("\nIndica a quantidade em Euro: "))
                dolar = euro*dec(1.08)
                print(f"Convertido: {euro:.2f}€ -> {dolar:.2f}$")
            case '2':
                dolar = dec(input("\nIndica a quantidade em Dolar: "))
                euro = dolar*dec(0.92)
                print(f"Convertido: {dolar:.2f}$ -> {euro:.2f}€")
            case _:
                print("Opção inválida.")
        
        opt_final = input("Pretende continuar a converter? (S/N) ")

        if opt_final == "N" or opt_final == "n":
            break

if __name__ == "__main__":
    main()