'''
13. Acrescente a possibilidade de repetição ao programa anterior enquanto o utilizador não acertar. O
programa deve dar pistas ao utilizador. Se este estiver a três valores de distância, então o programa
indica que "está próximo", se estiver a um valor, o programa diz que "está muito próximo".
'''
import random

def main():
    num_magico = random.randrange(1, 21)
    # print(num_magico)
    num = 0

    while num != num_magico:
        num = int(input("Tenta adivinhar o número mágico: "))
        if num - num_magico == 3 or num_magico - num == 3 or num - num_magico == 2 or num_magico - num == 2:
            print("Estás próximo!")
        elif num + 1 == num_magico or num_magico + 1  == num:
            print("Estás muito próximo!")
        elif num == num_magico:
            print("Acertaste!")
        else:
            print("Erraste!")

if __name__ == "__main__":
    main()