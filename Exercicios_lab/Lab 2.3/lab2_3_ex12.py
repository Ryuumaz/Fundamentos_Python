'''
12. Investigue o módulo random e acrescente possibilidade de o número mágico ser um número (pseudo)
aleatório entre 1 e 20.
'''
import random

def main():
    num_magico = random.randrange(1, 21)
    print(num_magico)
    num = int(input("Tenta adivinhar o número mágico: "))

    if num < num_magico:
        print("O número mágico é maior!")
    elif num > num_magico:
        print("O número mágico é menor!")
    elif num == num_magico:
        print("Acertaste!")


if __name__ == "__main__":
    main()